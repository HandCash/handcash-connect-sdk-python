from .api import HandCashConnectService, HttpRequestFactory
from .profile import Profile
from .environments import Environment


class HandcashCloudAccount:
    def __init__(self, profile):
        self.profile = profile

    @staticmethod
    def from_auth_token(auth_token: str, environment: Environment):
        handcash_connect_service = HandCashConnectService(HttpRequestFactory(auth_token, environment.api_endpoint))

        return HandcashCloudAccount(Profile(handcash_connect_service))
