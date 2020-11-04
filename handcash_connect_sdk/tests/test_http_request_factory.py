import pytest
import json
from freezegun import freeze_time
from handcash_connect_sdk.api import HttpRequestFactory


@pytest.fixture(name='http_request_factory')
def http_request_factory_fixture():
    auth_token = "2343a7caf0703b50f18b5dbd580f2fcc4cf489d608f9802cb917517e1c94a5e1"
    base_api_endpoints = "https://beta-cloud.handcash.io"
    http_request_factory = HttpRequestFactory(auth_token, base_api_endpoints)

    return http_request_factory


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_current_profile_request(http_request_factory: HttpRequestFactory):
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/currentUserProfile",
        json.dumps({}),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3045022100a7d5acd354204df634481c464e9125c43c0051e92a16549f67de0bc3987d1b2102203a193bfa1ff8a293fe450fac1ea924fe2c36c4e44106486cc384dec10b7b7a9a",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_current_profile_request()

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_public_profiles_by_handle_request(http_request_factory: HttpRequestFactory):
    aliases = ["testuser1"]
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/publicUserProfiles",
        json.dumps({"aliases": aliases}, separators=(',', ':')),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "304502210080f6bac88a96bbb4db7fb0272e665655752b18c1080efa9acfa7752c005231ac02202ddfe430a5b63166f04316236356d1cc9f4a7b2d8804f2e6fd748e50d4d1e5d0",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_public_profiles_by_handle_request(aliases)

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_user_friends_request(http_request_factory: HttpRequestFactory):
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/friends",
        json.dumps({}),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3044022062a07878c181b146ced853523e5972d025386dc435f87b93ee9f873c586d35870220515e25e2d80cae6b2490349c03025eeef7368391db06273721bf715237adb6d7",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_user_friends_request()

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_user_permissions_request(http_request_factory: HttpRequestFactory):
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/permissions",
        json.dumps({}),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3044022056c7514a39b615092b1c317468881d6545f956e454282ace07fe88817256bc4102205f98fdd18f86201c22c62a3815ef9cc653f2b15a8859b772d9ca908727a3d958",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_user_permissions_request()

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers



@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_encryption_keypair_request(http_request_factory: HttpRequestFactory):
    encryption_public_key = "123827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418108"
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/encryptionKeypair",
        json.dumps({"encryptionPublicKey": encryption_public_key}, separators=(',', ':')),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "304402207e42d5887a0be636905bf30280e74164fd4f7b9eb1284aed13ee8551fd978135022073cb1cc157b03039a7f0c3190b999924b05159b2597e3ccc6f1701cab1e4a68d",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_encryption_keypair_request(encryption_public_key)

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers


@freeze_time('2020-12-01T12:00:00.000Z', 1)
def test_get_spendable_balance_request(http_request_factory: HttpRequestFactory):
    currency_code = "USD"
    expected_url, expected_body, expected_headers = (
        "https://beta-cloud.handcash.io/v1/connect/profile/spendableBalance",
        json.dumps({"currencyCode": currency_code}, separators=(',', ':')),
        {
            "oauth-publickey": "033827aad966472d44dc230ec3163c78adf4a030fa03de729af50a62ca6c418109",
            "oauth-signature": "3045022100b5444df336acc2e632b2d7f0ac479a398122d76b4411ee6b41e392f25ad5b72f0220255792d33a2c17f9a086fe577487718fc8de03bb991c07a6933f7447786febb9",
            "oauth-timestamp": "2020-12-01T12:00:00.000Z"
        })

    url, body, headers = http_request_factory.get_spendable_balance_request(currency_code)

    assert expected_url == url
    assert expected_body == body
    assert expected_headers == headers
