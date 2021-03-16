from attr import attrs, attrib


@attrs(slots=True)
class SpendableBalance:
    spendableSatoshiBalance: int = attrib()
    spendableFiatBalance: float = attrib()
    currencyCode: str = attrib()
