from enum import Enum

class MoodCauseTypes(str, Enum):
    FAMILY = "family"
    FINANCE = "finance"
    FREETIME = "freetime"
    HEALTH = "health"
    PRIVATE = "private"
    RELATIONSHIP = "relationship"
    SOCIAL = "social"
    WORK = "work"