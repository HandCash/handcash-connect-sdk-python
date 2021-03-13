from typing import List

from bitcoinx import PrivateKey

from .api import HandCashConnectService
from .entities.encryption_keypair import EncryptionKeypair
from .entities.user_profile import UserProfile, UserPublicProfile


class Profile:
    def __init__(self, handcash_connect_service: HandCashConnectService):
        self._handcash_connect_service = handcash_connect_service

    def get_current_profile(self) -> UserProfile:
        return UserProfile(**self._handcash_connect_service.get_current_profile())

    def get_public_profiles_by_handle(self, handles) -> List[UserPublicProfile]:
        return [UserPublicProfile(**user_profile) for
                user_profile in self._handcash_connect_service.get_public_profiles_by_handle(handles)["items"]]

    def get_friends(self) -> List[UserPublicProfile]:
        return [UserPublicProfile(**user_profile) for
                user_profile in self._handcash_connect_service.get_user_friends()["items"]]

    def get_permissions(self) -> List[str]:
        return self._handcash_connect_service.get_user_permissions()["items"]

    def get_encryption_keypair(self) -> EncryptionKeypair:
        private_key = PrivateKey.from_random()
        public_key = private_key.public_key
        encryption_keypair = self._handcash_connect_service.get_encryption_keypair(public_key.to_hex())
        return EncryptionKeypair(
            privateKey=private_key.decrypt_message(
                bytes.fromhex(encryption_keypair["encryptedPrivateKeyHex"])).decode("utf-8"),
            publicKey=private_key.decrypt_message(
                bytes.fromhex(encryption_keypair["encryptedPublicKeyHex"])).decode("utf-8"),
        )
