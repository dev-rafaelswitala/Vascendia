from enum import Enum

class ImmuneBoostTypes(str, Enum):
    EXERCISE = "exercise"
    HYDRATION = "hydration"
    HYGIENE = "hygiene"
    NUTRITION = "nutrition"
    SLEEP = "sleep"
    STRESS_MANAGEMENT = "stress_management"
    SUNLIGHT = "sunlight"
    VACCINATION = "vaccination"