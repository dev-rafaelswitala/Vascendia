from enum import Enum

class ServingTemperatureTypes(str, Enum):
    COLD = "cold"
    HOT = "hot"
    LUKEWARM = "lukewarm"
    WARM = "warm"