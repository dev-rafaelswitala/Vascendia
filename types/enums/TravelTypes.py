from enum import Enum

class TravelTypes(str, Enum):
    ADVENTURE = "adventure"
    BUSINESS = "business"
    CULTURAL = "cultural"
    FAMILY = "family"
    LEISURE = "leisure"
    NATURE = "nature"
    STAYCATION = "staycation"