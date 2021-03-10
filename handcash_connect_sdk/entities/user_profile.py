from attr import attrs, attrib


@attrs(slots=True)
class UserPrivateProfile:
    email: str = attrib()
    phoneNumber: str = attrib(default="")


@attrs(slots=True)
class UserPublicProfile:
    id: str = attrib()
    handle: str = attrib(default="")
    displayName: str = attrib(default="")
    avatarUrl: str = attrib(default="")
    paymail: str = attrib(default="")
    localCurrencyCode: str = attrib(default="")


@attrs(slots=True)
class UserProfile:
    publicProfile: UserPublicProfile = attrib(
        converter=lambda self: UserPublicProfile(**self),
    )
    privateProfile: UserPrivateProfile = attrib(
        converter=lambda self: UserPrivateProfile(**self),
    )
