from enum import Enum

class RouteTypes(str, Enum):
    ASPHALT = "asphalt"
    CITY = "city"
    DIRT_ROAD = "dirt_road"
    FIELD_PATH = "field_path"
    FOREST_ROAD = "forest_road"
    GRAVEL = "gravel"
    MIX = "mix"
    MOUNTAIN = "mountain"
    NATURE = "nature"
    PARK = "park"
    ROAD = "road"