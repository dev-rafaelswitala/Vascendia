from enum import Enum

class SavingGoalTypes(str, Enum):
    BIG_PURCHASE = "big_purchase"
    EMERGENCY_FUND = "emergency_fund"
    INVESTMENTS = "investments"
    RETIREMENT = "retirement"
    TRIP = "trip"
    VACATION = "vacation"