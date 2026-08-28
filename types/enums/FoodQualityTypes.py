from enum import Enum

class FoodQualityTypes(str, Enum):
    BALANCED = "balanced"
    FAST_FOOD = "fast_food"
    HEALTHY = "healthy"
    HOME_MADE = "home_made"
    NEUTRAL = "neutral"
    UNHEALTHY = "unhealthy"
    VERY_HEALTHY = "very_healthy"
    VERY_UNHEALTHY = "very_unhealthy"