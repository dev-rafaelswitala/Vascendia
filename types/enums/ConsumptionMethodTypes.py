from enum import Enum

class ConsumptionMethodTypes(str, Enum):
    DRINKING = "drinking"
    EATING = "eating"
    INHALATION = "inhalation"
    INJECTION = "injection"
    NASAL = "nasal"
    ORAL = "oral"
    PLUGGING = "plugging"
    SMOKE = "smoke"
    SUBLINGUAL = "sublingual"
    TOPICAL = "topical"
    VAPING = "vaping"