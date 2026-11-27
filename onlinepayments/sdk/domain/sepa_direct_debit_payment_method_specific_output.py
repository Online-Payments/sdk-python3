#
# This file was automatically generated.
#
from .data_object import DataObject
from .fraud_results import FraudResults
from .payment_product771_specific_output import PaymentProduct771SpecificOutput


class SepaDirectDebitPaymentMethodSpecificOutput(DataObject):

    __slots__ = (
        "__fraud_results",
        "__payment_product771_specific_output",
        "__payment_product_id",
    )

    __fraud_results: FraudResults | None
    __payment_product771_specific_output: PaymentProduct771SpecificOutput | None
    __payment_product_id: int | None

    def __init__(
        self,
        *,
        fraud_results: FraudResults | None = None,
        payment_product771_specific_output: PaymentProduct771SpecificOutput | None = None,
        payment_product_id: int | None = None,
    ) -> None:
        self.fraud_results = fraud_results
        self.payment_product771_specific_output = payment_product771_specific_output
        self.payment_product_id = payment_product_id

    @property
    def fraud_results(self) -> FraudResults | None:
        """
        | Object containing the results of the fraud screening

        Type: :class:`onlinepayments.sdk.domain.fraud_results.FraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: FraudResults | None) -> None:
        self.__fraud_results = value

    @property
    def payment_product771_specific_output(self) -> PaymentProduct771SpecificOutput | None:
        """
        | Output that is SEPA Direct Debit specific (i.e. the used mandate)

        Type: :class:`onlinepayments.sdk.domain.payment_product771_specific_output.PaymentProduct771SpecificOutput`
        """
        return self.__payment_product771_specific_output

    @payment_product771_specific_output.setter
    def payment_product771_specific_output(self, value: PaymentProduct771SpecificOutput | None) -> None:
        self.__payment_product771_specific_output = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.payment_product771_specific_output is not None:
            dictionary['paymentProduct771SpecificOutput'] = self.payment_product771_specific_output.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SepaDirectDebitPaymentMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'paymentProduct771SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct771SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct771SpecificOutput']))
            value = PaymentProduct771SpecificOutput()
            self.payment_product771_specific_output = value.from_dictionary(dictionary['paymentProduct771SpecificOutput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
