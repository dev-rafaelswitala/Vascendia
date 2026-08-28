from enum import Enum

class SessionInputTypes(str, Enum):
    INPUT_FIELDS = "input_fields"
    QUESTIONNAIRE = "questionnaire"
    TABLE = "table"