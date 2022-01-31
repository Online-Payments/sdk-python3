from onlinepayments.sdk.api_exception import ApiException


class PaymentPlatformException(ApiException):
    """
    Represents an error response from the payment platform when something
    went wrong at the payment platform or further downstream.
    """

    def __init__(self, status_code, response_body, error_id, errors, message="the Online Payments platform returned an error response"):
        super(PaymentPlatformException, self).__init__(status_code, response_body, error_id, errors, message)
