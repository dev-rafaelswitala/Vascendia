from enum import Enum

class SwimmingStyleTypes(str, Enum):
    BACKSTROKE = "backstroke"
    BREASTSTROKE = "breaststroke"
    BUTTERFLY = "butterfly"
    DOLPHIN_KICK = "dolphin_kick"
    FREETIME = "freetime"
    FRONT_CRAWL = "front_crawl"
    MIX = "mix"
    TECHNIQUE = "technique"