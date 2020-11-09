import requests
import logging
from requests.exceptions import RequestException
from .http_request_factory import HttpRequestFactory
from .handcash_connect_api_error import HandCashConnectApiError


class HandCashConnectService:
    def __init__(self, http_request_factory: HttpRequestFactory):
        self._http_request_factory = http_request_factory

    def get_current_profile(self):
        return self._handle_http_request(
            *self._http_request_factory.get_current_profile_request())

    def get_public_profiles_by_handle(self, handles: list):
        return self._handle_http_request(
            *self._http_request_factory.get_public_profiles_by_handle_request(handles))

    def get_user_permissions(self):
        return self._handle_http_request(
            *self._http_request_factory.get_user_permissions_request())

    def get_encryption_keypair(self, encryption_public_key):
        return self._handle_http_request(
            *self._http_request_factory.get_encryption_keypair_request(encryption_public_key))

    def get_user_friends(self):
        return self._handle_http_request(
            *self._http_request_factory.get_user_friends_request())

    def get_spendable_balance(self, currency_code):
        return self._handle_http_request(
            *self._http_request_factory.get_spendable_balance_request(currency_code))

    @staticmethod
    def _handle_http_request(method: str, url: str, body: dict, headers: dict):
        try:
            logging.debug(f"{method} request to {url}. Body: {body}, headers: {headers}")

            response = requests.request(method, url, json=body, headers=headers)
            response.raise_for_status()

            logging.debug(f"Response: {response.json()}")

            return response.json()
        except RequestException as exc:
            reason = exc.response.reason
            if isinstance(reason, bytes):
                try:
                    reason = reason.decode('utf-8')
                except UnicodeDecodeError:
                    reason = reason.decode('iso-8859-1')
            raise HandCashConnectApiError(exc.response.status_code, reason)