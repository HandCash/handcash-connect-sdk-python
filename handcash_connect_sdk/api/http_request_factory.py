import json
from bitcoinx.keys import PrivateKey
from datetime import datetime, timezone


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
    def _get_request_signature(method: str, endpoint: str, body: str, timestamp: datetime, private_key: PrivateKey):
        signature_hash = f"{method}\n{endpoint}\n{timestamp}\n{body}"
        return private_key.sign(bytes(signature_hash, 'utf-8')).hex()

    def _get_signed_request(self, method, endpoint, body={}):
        timestamp = self._isoformat_js(datetime.now())
        private_key = PrivateKey.from_hex(self._auth_token)
        public_key = private_key.public_key #  PublicKey(private_key._secp256k1_public_key(), True)

        return (
            method,
            f"{self._base_api_endpoint}{endpoint}",
            body,
            {
                'oauth-publickey': public_key.to_hex(),
                'oauth-signature': self._get_request_signature(method, endpoint, json.dumps(body, separators=(',', ':')), timestamp, private_key),
                'oauth-timestamp': timestamp
            }  # headers
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
            { 'aliases': aliases }
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
            { "encryptionPublicKey": encryption_public_key }
        )

    def get_spendable_balance_request(self, currency_code: str):
        return self._get_signed_request(
            'GET',
            f"{HttpRequestFactory.PROFILE_ENDPOINT}/spendableBalance",
            { "currencyCode": currency_code }
        )
