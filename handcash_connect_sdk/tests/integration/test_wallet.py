import os
import unittest

from handcash_connect_sdk import environments, HandcashCloudAccount
from handcash_connect_sdk import PaymentParameters, PayTo, Attachment
from handcash_connect_sdk.api import HandCashConnectApiError


class TestWallet(unittest.TestCase):

    def setUp(self):
        auth_token = os.environ["HC_AUTH_TOKEN"]
        handcash_cloud_account = HandcashCloudAccount.from_auth_token(auth_token, environments.PROD)
        self.wallet = handcash_cloud_account.wallet

    def test_pay(self):
        payment_parameters = PaymentParameters(
            description='Test Connect SDK',
            appAction='test',
            receivers=[
                PayTo(sendAmount=0.01, currencyCode='USD', destination='rjseibane'),
            ],
            attachment=Attachment(format='json', value={"key": "value"})
        )
        payment_result = self.wallet.pay(payment_parameters)
        assert payment_result is not None

    def test_pay_with_minimal_parameters(self):
        payment_parameters = PaymentParameters(
            description='Testing SDK',
            receivers=[
                PayTo(sendAmount=0.01, currencyCode='USD', destination='rjseibane'),
            ],
        )
        payment_result = self.wallet.pay(payment_parameters)
        assert payment_result is not None

    def test_pay_should_fail(self):
        payment_parameters = PaymentParameters(
            description='Testing SDK',
            appAction='',
            receivers=[
                PayTo(sendAmount=0.01, currencyCode='USD', destination='rjseibane'),
            ],
        )
        self.assertRaises(HandCashConnectApiError, self.wallet.pay, payment_parameters)

    def test_get_payment(self):
        transaction_id = '5b4bf89642b42f479f2dfd6f13e3b33cfb854f9581d3275614c79ba291da3ceb'
        payment_result = self.wallet.get_payment(transaction_id)
        assert payment_result is not None

    def test_get_spendable_balance(self):
        spendable_balance = self.wallet.get_spendable_balance(currency_code='EUR')
        assert spendable_balance is not None
