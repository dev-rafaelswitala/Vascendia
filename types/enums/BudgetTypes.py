from enum import Enum

class BudgetTypes(str, Enum):
    DEBT = "debt"
    EXPENSE = "expense"
    INCOME = "income"
    INVESTMENTS = "investment"
    SAVINGS = "savings"