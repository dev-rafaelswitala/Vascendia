from enum import Enum

class IncomeTypes(str, Enum):
    FREELANCE = "freelance"
    GIFTS = "gifts"
    INVESTMENTS = "investments"
    SALARY = "salary"