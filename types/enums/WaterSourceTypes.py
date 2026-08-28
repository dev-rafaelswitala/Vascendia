from enum import Enum

class WaterSourceTypes(str, Enum):
    BOTTLED_WATER = "bottled_water"
    MINERAL_WATER = "mineral_water"
    SPARKLING_WATER = "sparkling_water"
    SPRING_WATER = "spring_water"
    TAP_WATER = "tap_water"