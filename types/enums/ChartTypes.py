from enum import Enum

class ChartTypes(str, Enum):
    BAR = "bar"
    DONUT = "donut"
    ENUM_BAR = "enum_bar"
    LINE = "line"
    NONE = "none"
    PIE = "pie"
    REGRESSION = "regression"
    SCATTER = "scatter"
    VALUE = "value"