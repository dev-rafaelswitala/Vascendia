from enum import Enum

class DrinkingTypes(str, Enum):
    ALCOHOL = "alcohol"
    BEER = "beer"
    COCKTAIL = "cocktail"
    COFFEE = "coffee"
    ENERGY_DRINK = "energy_drink"
    JUICE = "juice"
    LEMONADE = "lemonade"
    MILK = "milk"
    SMOOTHIE = "smoothie"
    TEA = "tea"
    WATER = "water"
    WINE = "wine"