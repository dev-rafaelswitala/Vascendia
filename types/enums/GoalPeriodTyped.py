from enum import Enum

class GoalPeriodTyped(str, Enum):
    EVERY_HOUR = "every_hour"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    DATE_RANGE = "date_range"