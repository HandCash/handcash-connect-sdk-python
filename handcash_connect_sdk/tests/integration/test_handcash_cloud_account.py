import os

from handcash_connect_sdk import HandcashCloudAccount, environments


def test_api_authorization():
    auth_token = os.environ["HC_AUTH_TOKEN"]
    app_secret = os.environ["HC_APP_SECRET"]
    handcash_cloud_account = HandcashCloudAccount.from_auth_token(auth_token, app_secret, environments.PROD)
    handcash_cloud_account.profile.get_current_profile()
