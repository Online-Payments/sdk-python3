import logging
from typing import Iterable, Tuple

from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.json.marshaller_syntax_exception import MarshallerSyntaxException
from onlinepayments.sdk.webhooks.api_version_mismatch_exception import ApiVersionMismatchException
from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException
from onlinepayments.sdk.webhooks.webhooks_helper import WebhooksHelper

from webhooks_setup import WebhookInbox

logger = logging.getLogger(__name__)


class WebhooksEndpoint:

    def __init__(self, webhooks_helper: WebhooksHelper, inbox: WebhookInbox):
        self.__webhooks_helper = webhooks_helper
        self.__inbox = inbox

    # [START webhooks-receive]
    # Call this from your HTTP endpoint with the raw body and the request headers, e.g. in Flask:
    #   @app.post("/webhooks")
    #   def webhooks():
    #       return "", endpoint.receive(request.get_data(), request.headers.items())
    # In Django use request.body and request.headers.items(); in FastAPI await request.body() and
    # request.headers.items(). Pass the body unchanged, as bytes: parsing it as JSON first breaks the signature
    # check, and the SDK's helper needs bytes.
    # Returns the HTTP status to answer with.
    def receive(self, body: bytes, headers: Iterable[Tuple[str, str]]) -> int:
        # Pass every received pair as its own header, never merge repeated headers: a merged value would hide
        # the duplicate X-GCS-Signature or X-GCS-KeyId that the helper rejects.
        request_headers = [RequestHeader(name, value) for name, value in headers]
        try:
            # Checks the X-GCS-Signature and X-GCS-KeyId headers before parsing the event.
            webhooks_event = self.__webhooks_helper.unmarshal(body, request_headers)
        except SignatureValidationException:
            # Wrong or missing signature, or an unknown key ID (SecretKeyNotAvailableException, a subclass).
            # Not sent by the platform, or the wrong secret is configured. Do nothing with it.
            return 401
        except (ApiVersionMismatchException, MarshallerSyntaxException):
            # The signature is valid, so the platform sent it, but this SDK version cannot read it (another API
            # version, or a malformed body). Neither exception is a SignatureValidationException. An error
            # status would only make the platform send the same body again. Save the raw body, replay it after
            # you upgrade the SDK, and alert someone.
            self.__inbox.save_unreadable(body)
            logger.critical("ALERT: verified webhook event cannot be read, raw body saved (%d bytes)", len(body),
                            exc_info=True)
            return 200

        # Save the event first, then answer. Do not count on the platform sending the event again after a 2xx,
        # so an event that is only in memory when the process dies can be lost. Process it in a background job.
        self.__inbox.save_event(webhooks_event)
        return 200
    # [END webhooks-receive]
