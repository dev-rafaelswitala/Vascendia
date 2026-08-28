from enum import Enum

class ObstacleTypes(str, Enum):
    BOREDOM = "boredom"
    DIVERSION = "diversion"
    DOUBT = "doubt"
    EMOTIONAL_CAUSE = "emotional_cause"
    FATIGUE = "fatigue"
    HABIT = "habit"
    HEALTH_PROBLEMS = "health_problems"
    LACK_OF_TIME = "lack_of_time"
    LACK_OF_MOTIVATION = "lack_of_motivation"
    LACK_OF_RESOURCES = "lack_of_resources"
    NO_REASON = "no_reason"
    SOCIAL_CAUSE = "social_cause"
    STRESS = "stress"
    UNKNOWN = "unknown"
    WEATHER = "weather"