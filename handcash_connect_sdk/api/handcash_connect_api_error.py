class HandCashConnectApiError(Exception):
    def __init__(self, http_status_code: int, message: str = '', info: dict = None):
        self.http_status_code = http_status_code
        self.message = message
        self.info = info
