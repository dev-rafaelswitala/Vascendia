from enum import Enum

class VolunteeringTypes(str, Enum):
    ANIMAL_CARE = "animal_care"
    COMMUNITY_SERVICE = "community_service"
    EDUCATION = "education"
    ENVIRONMENTAL = "environmental"
    EVENT_SUPPORT = "event_support"
    HEALTHCARE = "healthcare"