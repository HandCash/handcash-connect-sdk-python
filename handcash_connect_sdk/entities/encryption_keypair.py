from attr import attrs, attrib


@attrs(slots=True)
class EncryptionKeypair:
    privateKey: str = attrib()
    publicKey: str = attrib()
