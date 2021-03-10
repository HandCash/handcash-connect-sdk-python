import json
from datetime import datetime, timezone
from urllib.parse import urlencode

from bitcoinx.keys import PrivateKey

from handcash_connect_sdk.entities.payment_parameters import PaymentParameters


class HttpRequestFactory:
    PROFILE_ENDPOINT = '/v1/connect/profile'
    WALLET_ENDPOINT = '/v1/connect/wallet'

    def __init__(self, auth_token: str, base_api_endpoint: str):
        self._auth_token = auth_token
        self._base_api_endpoint = base_api_endpoint

    @staticmethod
    def _isoformat_js(dt: datetime):
        return dt.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

    @staticmethod
    def _get_request_signature(method: str, endpoint: str, body: str, timestamp: str, private_key: PrivateKey):
        signature_hash = f"{method}\n{endpoint}\n{timestamp}\n{body}"
        return private_key.sign(bytes(signature_hash, 'utf-8')).hex()

    def _get_signed_request(self, method, endpoint, body=None, query_parameters=None):
        if body is None:
            body = {}
        timestamp = self._isoformat_js(datetime.now())
        private_key = PrivateKey.from_hex(self._auth_token)
        public_key = private_key.public_key

        endpoint = f"{endpoint}{'' if query_parameters is None else '?' + urlencode(query_parameters)}"

        return (
            method,
            f"{self._base_api_endpoint}{endpoint}",
            body,
            {
                'oauth-publickey': public_key.to_hex(),
                'oauth-signature': self._get_request_signature(method,
                                                               endpoint,
                                                               json.dumps(body),
                                                               timestamp,
                                                               private_key),
                'oauth-timestamp': timestamp
            }
        )

    def get_current_profile_request(self):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/currentUserProfile"
        )

    def get_public_profiles_by_handle_request(self, aliases: list):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/publicUserProfiles",
            body={'aliases': aliases}
        )

    def get_user_friends_request(self):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/friends"
        )

    def get_user_permissions_request(self):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/permissions"
        )

    def get_encryption_keypair_request(self, encryption_public_key: str):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/encryptionKeypair",
            body={"encryptionPublicKey": encryption_public_key}
        )

    def get_spendable_balance_request(self, currency_code: str):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/spendableBalance",
            body={"currencyCode": currency_code}
        )

    def get_pay_request(self, payment_parameters: PaymentParameters):
        return self._get_signed_request(
            'POST',
            f"{HttpRequestFactory.WALLET_ENDPOINT}/pay",
            body={
                "description": payment_parameters.description,
                "appAction": payment_parameters.appAction,
                "receivers": [item.__dict__ for item in payment_parameters.receivers],
                "attachment": payment_parameters.attachment.__dict__,
            },
        )

    def get_payment_request(self, transaction_id: str):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.WALLET_ENDPOINT}/payment",
            body={
                "transactionId": transaction_id,
            },
        )
