from . import environments
from .api import HandCashConnectService, HttpRequestFactory
from .environments import Environment
from .profile import Profile
from .wallet import Wallet


class HandcashCloudAccount:
    def __init__(self, profile: Profile, wallet: Wallet):
        self.profile = profile
        self.wallet = wallet

    @staticmethod
    def from_auth_token(auth_token: str, app_secret: str, environment: Environment = environments.PROD):
        handcash_connect_service = HandCashConnectService(
            HttpRequestFactory(auth_token, app_secret, environment.api_endpoint))

        return HandcashCloudAccount(Profile(handcash_connect_service), Wallet(handcash_connect_service))
