from enum import Enum

class ExpenseTypes(str, Enum):
    CHARITY = "charity"
    EDUCATION = "education"
    FOOD = "food"
    HEALTH = "health"
    HOUSING = "housing"
    INSURANCE = "insurance"
    LEISURE = "leisure"
    SHOPPING = "shopping"
    TRANSPORT = "transport"
    UTILITIES = "utilities"