from enum import Enum

class StatusTypes(str, Enum):
    ABORTED = "aborted"
    COMPLETED = "completed"
    PARTIALLY = "partially"
    STARTED = "started"