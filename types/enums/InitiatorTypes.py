from enum import Enum

class InitiatorTypes(str, Enum):
    FAMILY = "family"
    FOREIGN = "foreign"
    FRIENDS = "friends"
    MYSELF = "myself"
    PARTNER = "partner"