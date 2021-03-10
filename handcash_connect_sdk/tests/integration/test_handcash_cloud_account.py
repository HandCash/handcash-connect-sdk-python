import os

from handcash_connect_sdk import HandcashCloudAccount, environments


def test_api_authorization():
    auth_token = os.environ["HC_AUTH_TOKEN"]
    handcash_cloud_account = HandcashCloudAccount.from_auth_token(auth_token, environments.PROD)
    handcash_cloud_account.profile.get_current_profile()
