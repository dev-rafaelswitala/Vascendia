from enum import Enum

class FieldTypes(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    ENUM = "enum"
    INTEGER = "integer"
    NUMBER = "number"
    RANGE_0_10 = "range_0_10"
    RANGE_0_100 = "range_0_100"
    TEXT = "text"