from enum import Enum

class AlcoholTypes(str, Enum):
    BEER = "beer"
    CIDER = "cider"
    COCKTAIL = "cocktail"
    LONGDRINK = "longdrink"
    SPARKLING_WINE = "sparkling_wine"
    SPIRITS = "spirits"
    WINE = "wine"