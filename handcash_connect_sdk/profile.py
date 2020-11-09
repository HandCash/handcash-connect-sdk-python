from typing import List
from attr import attrs, attrib
from bitcoinx import PrivateKey, PublicKey
from .api import HandCashConnectService


@attrs
class UserPublicProfile:
    id: str = attrib()
    handle: str = attrib(default="")
    displayName: str = attrib(default="")
    avatarUrl: str = attrib(default="")
    localCurrencyCode: str = attrib(default="")
    paymail: str = attrib(default="")


@attrs
class UserPrivateProfile:
    email: str = attrib()
    phoneNumber: str = attrib(default="")


@attrs
class UserProfile:
    publicProfile: UserPublicProfile = attrib(
        converter=lambda self: UserPublicProfile(**self),
    )
    privateProfile: UserPrivateProfile = attrib(
        converter=lambda self: UserPrivateProfile(**self),
    )


@attrs
class EncryptionKeypair:
    privateKey: str = attrib()
    publicKey: str = attrib()


class Profile:
    def __init__(self, handcash_connect_service: HandCashConnectService):
        self._handcash_connect_service = handcash_connect_service

    def get_current_profilie(self) -> UserProfile:
        return UserProfile(**self._handcash_connect_service.get_current_profile())

    def get_public_profiles_by_handle(self, handles) -> List[UserPublicProfile]:
        return [UserPublicProfile(**user_profile) for
                user_profile in self._handcash_connect_service.get_public_profiles_by_handle(handles)["items"]]

    def get_friends(self) -> List[UserPublicProfile]:
        return [UserPublicProfile(**user_profile) for
                user_profile in self._handcash_connect_service.get_user_friends()["items"]]

    def get_permissions(self) -> List[str]:
        return self._handcash_connect_service.get_user_permissions()["items"]

    def get_encryption_keypair(self):
        private_key = PrivateKey.from_hex("50e83102c35df17e0914168c92f383a71e52ac8a8df5eefaee29bab36bc2fb09") #PrivateKey.from_random()
        public_key = PublicKey(private_key._secp256k1_public_key(), False)
        encryption_keypair = self._handcash_connect_service.get_encryption_keypair(public_key.to_hex())
        return EncryptionKeypair(
            privateKey=private_key.decrypt_message(
                bytes.fromhex(encryption_keypair["encryptedPrivateKeyHex"])).decode("utf-8"),
            publicKey=private_key.decrypt_message(
                bytes.fromhex(encryption_keypair["encryptedPublicKeyHex"])).decode("utf-8"),
        )
