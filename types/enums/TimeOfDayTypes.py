from enum import Enum

class TimeOfDayTypes(str, Enum):
    AFTERNOON = "afternoon"
    EVENING = "evening"
    LATE_MORNING = "late_morning"
    MIDDAY = "midday"
    MORNING = "morning"
    NIGHT = "night"