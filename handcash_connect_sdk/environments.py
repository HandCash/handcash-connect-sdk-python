from typing import NamedTuple, Final


class Environment(NamedTuple):
    api_endpoint: str
    client_url: str


BETA: Final[Environment] = Environment(
    api_endpoint="https://beta-cloud.handcash.io",
    client_url="https://beta-app.handcash.io",
)

IAE: Final[Environment] = Environment(
    api_endpoint="https://iae.cloud.handcash.io",
    client_url="https://iae-app.handcash.io",
)

PROD: Final[Environment] = Environment(
    api_endpoint="https://cloud.handcash.io",
    client_url="https://app.handcash.io",
)
