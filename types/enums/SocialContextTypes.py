from enum import Enum

class SocialContextTypes(str, Enum):
    ACQUAINTANCE = "acquaintance"
    ALONE = "alone"
    COLLEAGUES = "colleagues"
    GROUP = "group"
    FAMILY = "family"
    FOREIGN = "foreign"
    FRIENDS = "friends"
    PARTNER = "partner"
    PUBLIC = "public"