from enum import Enum

class HealthCheckTypes(str, Enum):
    BLOOD_TEST = "blood_test"
    DENTAL = "dental"
    EYE = "eye"
    GENERAL_CHECKUP = "general_checkup"
    PHYSICAL_FITNESS = "physical_fitness"
    SCREENING = "screening"
    SPECIALIST = "specialist"
    VACCINATION = "vaccination"