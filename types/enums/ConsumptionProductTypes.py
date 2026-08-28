from enum import Enum

class ConsumptionProductTypes(str, Enum):
    CIGAR = "cigar"
    CIGARETTE = "cigarette"
    E_CIGARETTE = "e_cigarette"
    PIPE = "pipe"
    SHISHA = "shisha"
    VAPE = "vape"