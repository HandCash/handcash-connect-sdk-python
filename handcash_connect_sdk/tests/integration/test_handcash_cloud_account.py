import os
from handcash_connect_sdk import HandcashCloudAccount, environments

def test_api_authorization():
    auth_token = os.environ["HC_AUTH_TOKEN"] #"3243a7caf0703b50f18b5dbd580f2fcc4cf489d608f9802cb917517e1c94a5e0"
    handcash_cloud_account = HandcashCloudAccount.from_auth_token(auth_token, environments.BETA)
    handcash_cloud_account.profile.get_current_profilie()