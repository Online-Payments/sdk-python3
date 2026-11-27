#
# This file was automatically generated.
#
from .customer_bank_account import CustomerBankAccount
from .data_object import DataObject
from .fraud_results import FraudResults
from .payment_product3203_specific_output import PaymentProduct3203SpecificOutput
from .payment_product3204_specific_output import PaymentProduct3204SpecificOutput
from .payment_product5001_specific_output import PaymentProduct5001SpecificOutput
from .payment_product5402_specific_output import PaymentProduct5402SpecificOutput
from .payment_product5500_specific_output import PaymentProduct5500SpecificOutput
from .payment_product840_specific_output import PaymentProduct840SpecificOutput


class RedirectPaymentMethodSpecificOutput(DataObject):

    __slots__ = (
        "__authorisation_code",
        "__customer_bank_account",
        "__fraud_results",
        "__payment_method3204_specific_output",
        "__payment_option",
        "__payment_product3203_specific_output",
        "__payment_product5001_specific_output",
        "__payment_product5402_specific_output",
        "__payment_product5500_specific_output",
        "__payment_product840_specific_output",
        "__payment_product_id",
        "__token",
    )

    __authorisation_code: str | None
    __customer_bank_account: CustomerBankAccount | None
    __fraud_results: FraudResults | None
    __payment_method3204_specific_output: PaymentProduct3204SpecificOutput | None
    __payment_option: str | None
    __payment_product3203_specific_output: PaymentProduct3203SpecificOutput | None
    __payment_product5001_specific_output: PaymentProduct5001SpecificOutput | None
    __payment_product5402_specific_output: PaymentProduct5402SpecificOutput | None
    __payment_product5500_specific_output: PaymentProduct5500SpecificOutput | None
    __payment_product840_specific_output: PaymentProduct840SpecificOutput | None
    __payment_product_id: int | None
    __token: str | None

    def __init__(
        self,
        *,
        authorisation_code: str | None = None,
        customer_bank_account: CustomerBankAccount | None = None,
        fraud_results: FraudResults | None = None,
        payment_method3204_specific_output: PaymentProduct3204SpecificOutput | None = None,
        payment_option: str | None = None,
        payment_product3203_specific_output: PaymentProduct3203SpecificOutput | None = None,
        payment_product5001_specific_output: PaymentProduct5001SpecificOutput | None = None,
        payment_product5402_specific_output: PaymentProduct5402SpecificOutput | None = None,
        payment_product5500_specific_output: PaymentProduct5500SpecificOutput | None = None,
        payment_product840_specific_output: PaymentProduct840SpecificOutput | None = None,
        payment_product_id: int | None = None,
        token: str | None = None,
    ) -> None:
        self.authorisation_code = authorisation_code
        self.customer_bank_account = customer_bank_account
        self.fraud_results = fraud_results
        self.payment_method3204_specific_output = payment_method3204_specific_output
        self.payment_option = payment_option
        self.payment_product3203_specific_output = payment_product3203_specific_output
        self.payment_product5001_specific_output = payment_product5001_specific_output
        self.payment_product5402_specific_output = payment_product5402_specific_output
        self.payment_product5500_specific_output = payment_product5500_specific_output
        self.payment_product840_specific_output = payment_product840_specific_output
        self.payment_product_id = payment_product_id
        self.token = token

    @property
    def authorisation_code(self) -> str | None:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: str | None) -> None:
        self.__authorisation_code = value

    @property
    def customer_bank_account(self) -> CustomerBankAccount | None:
        """
        | Data of customer bank account

        Type: :class:`onlinepayments.sdk.domain.customer_bank_account.CustomerBankAccount`
        """
        return self.__customer_bank_account

    @customer_bank_account.setter
    def customer_bank_account(self, value: CustomerBankAccount | None) -> None:
        self.__customer_bank_account = value

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
    def payment_method3204_specific_output(self) -> PaymentProduct3204SpecificOutput | None:
        """
        | BLIK (payment product 3204) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3204_specific_output.PaymentProduct3204SpecificOutput`
        """
        return self.__payment_method3204_specific_output

    @payment_method3204_specific_output.setter
    def payment_method3204_specific_output(self, value: PaymentProduct3204SpecificOutput | None) -> None:
        self.__payment_method3204_specific_output = value

    @property
    def payment_option(self) -> str | None:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: str | None) -> None:
        self.__payment_option = value

    @property
    def payment_product3203_specific_output(self) -> PaymentProduct3203SpecificOutput | None:
        """
        | PostFinancePay (payment product 3203) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3203_specific_output.PaymentProduct3203SpecificOutput`
        """
        return self.__payment_product3203_specific_output

    @payment_product3203_specific_output.setter
    def payment_product3203_specific_output(self, value: PaymentProduct3203SpecificOutput | None) -> None:
        self.__payment_product3203_specific_output = value

    @property
    def payment_product5001_specific_output(self) -> PaymentProduct5001SpecificOutput | None:
        """
        | Bizum (payment product 5001) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product5001_specific_output.PaymentProduct5001SpecificOutput`
        """
        return self.__payment_product5001_specific_output

    @payment_product5001_specific_output.setter
    def payment_product5001_specific_output(self, value: PaymentProduct5001SpecificOutput | None) -> None:
        self.__payment_product5001_specific_output = value

    @property
    def payment_product5402_specific_output(self) -> PaymentProduct5402SpecificOutput | None:
        """
        | Meal vouchers (payment product 5402) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product5402_specific_output.PaymentProduct5402SpecificOutput`
        """
        return self.__payment_product5402_specific_output

    @payment_product5402_specific_output.setter
    def payment_product5402_specific_output(self, value: PaymentProduct5402SpecificOutput | None) -> None:
        self.__payment_product5402_specific_output = value

    @property
    def payment_product5500_specific_output(self) -> PaymentProduct5500SpecificOutput | None:
        """
        | Multibanco (payment product 5500) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product5500_specific_output.PaymentProduct5500SpecificOutput`
        """
        return self.__payment_product5500_specific_output

    @payment_product5500_specific_output.setter
    def payment_product5500_specific_output(self, value: PaymentProduct5500SpecificOutput | None) -> None:
        self.__payment_product5500_specific_output = value

    @property
    def payment_product840_specific_output(self) -> PaymentProduct840SpecificOutput | None:
        """
        | PayPal (payment product 840) specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product840_specific_output.PaymentProduct840SpecificOutput`
        """
        return self.__payment_product840_specific_output

    @payment_product840_specific_output.setter
    def payment_product840_specific_output(self, value: PaymentProduct840SpecificOutput | None) -> None:
        self.__payment_product840_specific_output = value

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

    @property
    def token(self) -> str | None:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.payment_method3204_specific_output is not None:
            dictionary['paymentMethod3204SpecificOutput'] = self.payment_method3204_specific_output.to_dictionary()
        if self.payment_option is not None:
            dictionary['paymentOption'] = self.payment_option
        if self.payment_product3203_specific_output is not None:
            dictionary['paymentProduct3203SpecificOutput'] = self.payment_product3203_specific_output.to_dictionary()
        if self.payment_product5001_specific_output is not None:
            dictionary['paymentProduct5001SpecificOutput'] = self.payment_product5001_specific_output.to_dictionary()
        if self.payment_product5402_specific_output is not None:
            dictionary['paymentProduct5402SpecificOutput'] = self.payment_product5402_specific_output.to_dictionary()
        if self.payment_product5500_specific_output is not None:
            dictionary['paymentProduct5500SpecificOutput'] = self.payment_product5500_specific_output.to_dictionary()
        if self.payment_product840_specific_output is not None:
            dictionary['paymentProduct840SpecificOutput'] = self.payment_product840_specific_output.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'paymentMethod3204SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentMethod3204SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentMethod3204SpecificOutput']))
            value = PaymentProduct3204SpecificOutput()
            self.payment_method3204_specific_output = value.from_dictionary(dictionary['paymentMethod3204SpecificOutput'])
        if 'paymentOption' in dictionary:
            self.payment_option = dictionary['paymentOption']
        if 'paymentProduct3203SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct3203SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3203SpecificOutput']))
            value = PaymentProduct3203SpecificOutput()
            self.payment_product3203_specific_output = value.from_dictionary(dictionary['paymentProduct3203SpecificOutput'])
        if 'paymentProduct5001SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct5001SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5001SpecificOutput']))
            value = PaymentProduct5001SpecificOutput()
            self.payment_product5001_specific_output = value.from_dictionary(dictionary['paymentProduct5001SpecificOutput'])
        if 'paymentProduct5402SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct5402SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5402SpecificOutput']))
            value = PaymentProduct5402SpecificOutput()
            self.payment_product5402_specific_output = value.from_dictionary(dictionary['paymentProduct5402SpecificOutput'])
        if 'paymentProduct5500SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct5500SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5500SpecificOutput']))
            value = PaymentProduct5500SpecificOutput()
            self.payment_product5500_specific_output = value.from_dictionary(dictionary['paymentProduct5500SpecificOutput'])
        if 'paymentProduct840SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificOutput']))
            value = PaymentProduct840SpecificOutput()
            self.payment_product840_specific_output = value.from_dictionary(dictionary['paymentProduct840SpecificOutput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self
