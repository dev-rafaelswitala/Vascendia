from enum import Enum

class MealTypes(str, Enum):
    BREAKFAST = "breakfast"
    DINNER = "dinner"
    LUNCH = "lunch"
    SNACK = "snack"