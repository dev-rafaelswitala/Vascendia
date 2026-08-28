from enum import Enum

class SubstanceTypes(str, Enum):
    ALCOHOL = "alcohol"
    CAFFEINE = "caffeine"
    CANNABIS = "cannabis"
    EMPATHOGEN = "empathogen"
    DEPRESSANT = "depressant"
    DISSOCIATIVE = "dissociative"
    MEDICATION = "medication"
    NICOTINE = "nicotine"
    OPIOID = "opioid"
    PSYCHEDELIC = "psychedelic"
    STIMULANT = "stimulant"