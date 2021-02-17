from typing import NamedTuple, Final


class Environment(NamedTuple):
    api_endpoint: str
    client_url: str


BETA: Final[Environment] = Environment(
    api_endpoint="https://beta-cloud.handcash.io",
    client_url="https://handcash-web-beta.firebaseapp.com",
)

IAE: Final[Environment] = Environment(
    api_endpoint="https://iae.cloud.handcash.io",
    client_url="https://handcash-web.firebaseapp.com",
)

PROD: Final[Environment] = Environment(
    api_endpoint="https://cloud.handcash.io",
    client_url="https://app.handcash.io",
)
