from enum import Enum

class EatingContextTypes(str, Enum):
    ALONE = "alone"
    AWAY = "away"
    FAMILY = "family"
    FRIENDS = "friends"
    RESTAURANT = "restaurant"
    WORK = "work"