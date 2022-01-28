import pytest
from freezegun import freeze_time

from handcash_connect_sdk import environments
from handcash_connect_sdk.api import HttpRequestFactory


@pytest.fixture(name='http_request_factory')
def http_request_factory_fixture():
    auth_token = "2343a7caf0703b50f18b5dbd580f2fcc4cf489d608f9802cb917517e1c94a5e1"
    base_api_endpoints = environments.PROD.api_endpoint
    http_request_factory = HttpRequestFactory(auth_token, base_api_endpoints)

    return http_request_factory


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_current_profile_request(http_request_factory: HttpRequestFactory):
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/profile/currentUserProfile",
        {},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3045022100a7d5acd354204df634481c464e9125c43c0051e92a16549f67de0bc3987d1b2102203a193bfa1ff8a293fe450fac1ea924fe2c36c4e44106486cc384dec10b7b7a9a",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_current_profile_request()

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_public_profiles_by_handle_request(http_request_factory: HttpRequestFactory):
    aliases = ["testuser1"]
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/profile/publicUserProfiles",
        {"aliases": aliases},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "304502210095a29dce87c06be7992299f7c67324bf4c1dc6fbb8bd8172f710f9b92b1e91010220478f1cfb834b770b479659c61d875717d9833bddef6f6a6acdeba6f74597e546",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_public_profiles_by_handle_request(aliases)

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_user_friends_request(http_request_factory: HttpRequestFactory):
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/profile/friends",
        {},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3044022062a07878c181b146ced853523e5972d025386dc435f87b93ee9f873c586d35870220515e25e2d80cae6b2490349c03025eeef7368391db06273721bf715237adb6d7",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_user_friends_request()

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_user_permissions_request(http_request_factory: HttpRequestFactory):
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/profile/permissions",
        {},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3044022056c7514a39b615092b1c317468881d6545f956e454282ace07fe88817256bc4102205f98fdd18f86201c22c62a3815ef9cc653f2b15a8859b772d9ca908727a3d958",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_user_permissions_request()

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_encryption_keypair_request(http_request_factory: HttpRequestFactory):
    encryption_public_key = "123827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418108"
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/profile/encryptionKeypair",
        {"encryptionPublicKey": encryption_public_key},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3045022100a2ac1fe44dfc0cfef52bd62461f1200619c47af92bb6347983eea71c460f37a20220610ad5a68d7f17e4d55301a836b1b97ca217969f2c12e79ee6901b3ce9fe7e3f",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_encryption_keypair_request(encryption_public_key)

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_spendable_balance_request(http_request_factory: HttpRequestFactory):
    currency_code = "USD"
    expected_method, expected_url, expected_body, expected_headers = (
        'GET',
        "https://cloud.handcash.io/v1/connect/wallet/spendableBalance",
        {"currencyCode": currency_code},
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "30450221008eff3d8c443ef74705516878c2eb78e398ed76407637381a37e5b611446f9a8502200462c80b0efeff64322c9a4388969cdac7b804fb17fd1b14410965f463dfdef6",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    method, url, body, headers = http_request_factory.get_spendable_balance_request(currency_code)

    assert expected_method == method
    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers
