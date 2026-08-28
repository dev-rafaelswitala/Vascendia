from enum import Enum

class BreakTypes(str, Enum):
    FORCED = "forced"
    LONG = "long"
    SHORT = "short"
    VOLUNTARY = "voluntary"