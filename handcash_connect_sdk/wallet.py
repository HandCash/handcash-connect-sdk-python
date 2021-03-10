from .api import HandCashConnectService
from .entities.payment_parameters import PaymentParameters
from .entities.payment_result import PaymentResult


class Wallet:
    def __init__(self, handcash_connect_service: HandCashConnectService):
        self._handcash_connect_service = handcash_connect_service

    def pay(self, payment_parameters: PaymentParameters) -> PaymentResult:
        return PaymentResult(**self._handcash_connect_service.pay(payment_parameters))

    def get_payment(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(**self._handcash_connect_service.get_payment(transaction_id))
