import os
import pytest
from handcash_connect_sdk.profile import Profile, UserProfile
from handcash_connect_sdk.api import HttpRequestFactory, HandCashConnectService


@pytest.fixture(name='profile')
def profile_fixture():
    auth_token = os.environ["HC_AUTH_TOKEN"]
    base_api_endpoints = "https://beta-cloud.handcash.io"
    http_request_factory = HttpRequestFactory(auth_token, base_api_endpoints)
    handcash_connect_service = HandCashConnectService(http_request_factory)
    profile = Profile(handcash_connect_service)

    return profile


@pytest.fixture(name='test_user_profile')
def test_user_profile_fixture():
    test_user_profile = UserProfile(
        publicProfile={
            "id": '5fa1e46ff767e70cb312000b',
            "handle": 'krzysiek',
            "displayName": '',
            "avatarUrl": 'https://beta-cloud.handcash.io/users/profilePicture/krzysiek',
            "localCurrencyCode": 'USD',
            "paymail": 'krzysiek@beta.handcash.io'},
        privateProfile={
            "email": 'krzysztof.fonal@codepoets.it',
            "phoneNumber": '+48726007079',
        })

    return test_user_profile


def test_get_current_profile(profile: Profile, test_user_profile: UserProfile):
    expected_user_profile = test_user_profile
    user_profile = profile.get_current_profilie()
    assert expected_user_profile == user_profile


def test_get_public_profiles_by_handle(profile: Profile, test_user_profile: UserProfile):
    expected_user_profile = test_user_profile.publicProfile
    handles = ['krzysiek']
    user_profiles = profile.get_public_profiles_by_handle(handles)
    assert len(user_profiles) == 1
    assert expected_user_profile == user_profiles[0]


def test_get_friends(profile: Profile):
    user_profiles = profile.get_friends()
    assert '+48726007079' == user_profiles


def test_get_permissions(profile: Profile):
    permissions = profile.get_permissions()
    assert ['PAY', 'USER_PRIVATE_PROFILE', 'DECRYPT'] == permissions


def test_get_encryption_keypair(profile: Profile):
    keypair = profile.get_encryption_keypair()
    assert "L1dBK2pHcxNZy3dFKLZMVtTq5wTBYzeBhubVBSYqmaKgXKi9Fthf" == keypair.privateKey
    assert "020410738217ca7c07937970b46e68275da98ef8227669fd0049b19b47cbcaa24a" == keypair.publicKey