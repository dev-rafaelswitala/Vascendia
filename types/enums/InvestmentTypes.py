from enum import Enum

class InvestmentTypes(str, Enum):
    BOND = "bond"
    COMMODITY = "commodity"
    CRYPTOCURRENCY = "cryptocurrency"
    ETF = "etf"
    MUTUAL_FUND = "mutual_fund"
    OTHER = "other"
    REAL_ESTATE = "real_estate"
    STOCK = "stock"