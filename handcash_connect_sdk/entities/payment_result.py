from typing import List

from attr import attrs, attrib

from handcash_connect_sdk.entities.payment_parameters import Attachment


@attrs(slots=True)
class PaymentParticipant:
    type: str = attrib()
    alias: str = attrib()
    displayName: str = attrib()
    profilePictureUrl: str = attrib()
    responseNote: str = attrib()


@attrs(slots=True)
class PaymentResult:
    transactionId: str = attrib()
    note: str = attrib()
    appAction: str = attrib()
    time: int = attrib()
    type: str = attrib()
    satoshiFees: int = attrib()
    satoshiAmount: int = attrib()
    fiatExchangeRate: float = attrib()
    fiatCurrencyCode: str = attrib()
    attachments: List[Attachment] = attrib(
        converter=lambda self: [Attachment(**item) for item in self],
        factory=list
    )
    participants: List[PaymentParticipant] = attrib(
        converter=lambda self: [PaymentParticipant(**item) for item in self],
        factory=list
    )
    rawTransactionHex: str = attrib(default='')
