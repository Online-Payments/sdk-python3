"""
Stand-ins for your application's own types and persistence. The examples use them where your code must store or read
data; replace them with your own code.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class OrderPaymentState(Enum):
    """
    The payment state of an order in your application.
    """
    PENDING = "pending"
    AUTHORIZED = "authorized"
    PAID = "paid"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
    REVERSED = "reversed"


@dataclass(frozen=True)
class PaymentStep:
    """
    What the web layer must do after a create payment call: redirect the customer to redirect_url, or show the state.
    """
    redirect_url: Optional[str] = None
    state: Optional[OrderPaymentState] = None


@dataclass(frozen=True)
class StoredHostedCheckout:
    hosted_checkout_id: str
    returnmac: str


class OrderStore(ABC):
    """
    Stand-in for your database code.
    """

    @abstractmethod
    def save_hosted_checkout(self, order_id: str, hosted_checkout_id: str, returnmac: str) -> None: ...

    @abstractmethod
    def get_hosted_checkout(self, order_id: str) -> StoredHostedCheckout: ...

    @abstractmethod
    def save_payment_id(self, order_id: str, payment_id: str) -> None: ...

    @abstractmethod
    def get_payment_id(self, order_id: str) -> Optional[str]:
        """
        None until a payment exists for the order.
        """

    @abstractmethod
    def save_idempotence_key(self, order_id: str, idempotence_key: str) -> None: ...

    @abstractmethod
    def get_idempotence_key(self, order_id: str) -> Optional[str]:
        """
        None until an idempotence key is stored for the order.
        """

    @abstractmethod
    def save_state(self, order_id: str, state: OrderPaymentState) -> None: ...

    @abstractmethod
    def save_recurring_payment_id(self, customer_id: str, initial_payment_id: str) -> None: ...

    @abstractmethod
    def get_recurring_payment_id(self, customer_id: str) -> str: ...


@dataclass(frozen=True)
class BrowserInfo:
    """
    Browser values collected with JavaScript on the checkout page.
    """
    color_depth: int
    java_enabled: bool
    screen_height: int
    screen_width: int
    timezone_offset_utc_minutes: int
    locale: str


@dataclass(frozen=True)
class CardInput:
    """
    Card details as entered by the customer. Never log or store this object.
    """
    number: str
    holder_name: str
    # MMYY, e.g. 1230 for December 2030.
    expiry_date: str
    cvv: str
