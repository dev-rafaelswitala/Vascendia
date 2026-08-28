from enum import Enum

class AnxietyReasonTypes(str, Enum):
    SOCIAL = "social"
    SUBSTANCE = "substance"
    TRAUMA = "trauma"
    UNKNOWN = "unknown"