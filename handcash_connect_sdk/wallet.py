from .api import HandCashConnectService
from .entities.payment_parameters import PaymentParameters
from .entities.payment_result import PaymentResult
from .entities.spendable_balance import SpendableBalance


class Wallet:
    def __init__(self, handcash_connect_service: HandCashConnectService):
        self._handcash_connect_service = handcash_connect_service

    def get_spendable_balance(self, currency_code: str = None) -> SpendableBalance:
        return SpendableBalance(**self._handcash_connect_service.get_spendable_balance(currency_code=currency_code))

    def pay(self, payment_parameters: PaymentParameters) -> PaymentResult:
        return PaymentResult(**self._handcash_connect_service.pay(payment_parameters))

    def get_payment(self, transaction_id: str) -> PaymentResult:
        return PaymentResult(**self._handcash_connect_service.get_payment(transaction_id))
