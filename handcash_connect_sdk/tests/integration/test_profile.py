import os
import unittest

from handcash_connect_sdk import environments, HandcashCloudAccount


class TestProfile(unittest.TestCase):

    def setUp(self):
        auth_token = os.environ["HC_AUTH_TOKEN"]
        handcash_cloud_account = HandcashCloudAccount.from_auth_token(auth_token, environments.PROD)
        self.profile = handcash_cloud_account.profile

    def test_get_current_profile(self):
        user_profile = self.profile.get_current_profile()
        assert user_profile is not None

    def test_get_public_profiles_by_handle(self):
        handles = ['krzysiek']
        user_profiles = self.profile.get_public_profiles_by_handle(handles)
        assert len(user_profiles) == 1
        assert user_profiles[0].handle == 'krzysiek'

    def test_get_friends(self):
        user_profiles = self.profile.get_friends()
        assert len(user_profiles) > 0

    def test_get_permissions(self):
        permissions = self.profile.get_permissions()
        expected = sorted(['PAY', 'USER_PRIVATE_PROFILE', 'DECRYPT', 'FRIENDS', 'USER_PUBLIC_PROFILE'])
        self.assertListEqual(expected, sorted(permissions))

    def test_get_encryption_keypair(self):
        keypair = self.profile.get_encryption_keypair()
        assert keypair is not None
