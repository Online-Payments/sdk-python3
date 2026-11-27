#
# This file was automatically generated.
#
from .data_object import DataObject
from .hosted_checkout_specific_output import HostedCheckoutSpecificOutput
from .operation_output import OperationOutput
from .payment_output import PaymentOutput
from .payment_status_output import PaymentStatusOutput
from .session_details import SessionDetails


class PaymentResponse(DataObject):

    __slots__ = (
        "__hosted_checkout_specific_output",
        "__id",
        "__operation_output",
        "__payment_output",
        "__session_details",
        "__status",
        "__status_output",
    )

    __hosted_checkout_specific_output: HostedCheckoutSpecificOutput | None
    __id: str | None
    __operation_output: OperationOutput | None
    __payment_output: PaymentOutput | None
    __session_details: SessionDetails | None
    __status: str | None
    __status_output: PaymentStatusOutput | None

    def __init__(
        self,
        *,
        hosted_checkout_specific_output: HostedCheckoutSpecificOutput | None = None,
        id: str | None = None,
        operation_output: OperationOutput | None = None,
        payment_output: PaymentOutput | None = None,
        session_details: SessionDetails | None = None,
        status: str | None = None,
        status_output: PaymentStatusOutput | None = None,
    ) -> None:
        self.hosted_checkout_specific_output = hosted_checkout_specific_output
        self.id = id
        self.operation_output = operation_output
        self.payment_output = payment_output
        self.session_details = session_details
        self.status = status
        self.status_output = status_output

    @property
    def hosted_checkout_specific_output(self) -> HostedCheckoutSpecificOutput | None:
        """
        | Hosted Checkout specific information. Populated if the payment was created on the platform through a Hosted Checkout.

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_output.HostedCheckoutSpecificOutput`
        """
        return self.__hosted_checkout_specific_output

    @hosted_checkout_specific_output.setter
    def hosted_checkout_specific_output(self, value: HostedCheckoutSpecificOutput | None) -> None:
        self.__hosted_checkout_specific_output = value

    @property
    def id(self) -> str | None:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def operation_output(self) -> OperationOutput | None:
        """
        | Object containing operation details

        Type: :class:`onlinepayments.sdk.domain.operation_output.OperationOutput`
        """
        return self.__operation_output

    @operation_output.setter
    def operation_output(self, value: OperationOutput | None) -> None:
        self.__operation_output = value

    @property
    def payment_output(self) -> PaymentOutput | None:
        """
        | Object containing payment details

        Type: :class:`onlinepayments.sdk.domain.payment_output.PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value: PaymentOutput | None) -> None:
        self.__payment_output = value

    @property
    def session_details(self) -> SessionDetails | None:
        """
        | Session context information. This denotes the origin of the payment session, where the session originated from and that session's unique identifier

        Type: :class:`onlinepayments.sdk.domain.session_details.SessionDetails`
        """
        return self.__session_details

    @session_details.setter
    def session_details(self, value: SessionDetails | None) -> None:
        self.__session_details = value

    @property
    def status(self) -> str | None:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str | None) -> None:
        self.__status = value

    @property
    def status_output(self) -> PaymentStatusOutput | None:
        """
        | This object has the numeric representation of the current payment status, the timestamp of the last status change, and the performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: PaymentStatusOutput | None) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.hosted_checkout_specific_output is not None:
            dictionary['hostedCheckoutSpecificOutput'] = self.hosted_checkout_specific_output.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.operation_output is not None:
            dictionary['operationOutput'] = self.operation_output.to_dictionary()
        if self.payment_output is not None:
            dictionary['paymentOutput'] = self.payment_output.to_dictionary()
        if self.session_details is not None:
            dictionary['sessionDetails'] = self.session_details.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentResponse':
        super().from_dictionary(dictionary)
        if 'hostedCheckoutSpecificOutput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificOutput']))
            value = HostedCheckoutSpecificOutput()
            self.hosted_checkout_specific_output = value.from_dictionary(dictionary['hostedCheckoutSpecificOutput'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'operationOutput' in dictionary:
            if not isinstance(dictionary['operationOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationOutput']))
            value = OperationOutput()
            self.operation_output = value.from_dictionary(dictionary['operationOutput'])
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutput()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'sessionDetails' in dictionary:
            if not isinstance(dictionary['sessionDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sessionDetails']))
            value = SessionDetails()
            self.session_details = value.from_dictionary(dictionary['sessionDetails'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
