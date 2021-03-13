from typing import List

from attr import attrs, attrib


@attrs(slots=False)
class PayTo:
    sendAmount: float = attrib()
    currencyCode: str = attrib()
    destination: str = attrib()


@attrs(slots=False)
class Attachment:
    format: str = attrib()
    value: any = attrib()


@attrs(slots=True)
class PaymentParameters:
    description: str = attrib()
    appAction: str = attrib()
    attachment: Attachment = attrib()
    receivers: List[PayTo] = attrib(factory=list)
