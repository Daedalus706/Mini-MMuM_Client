from enum import Enum

class TRIGGER(Enum):
    NONE = 0
    MATCH_START = 1
    ROUND_START = 2
    ROUND_END = 3
    MOVED_IN_OWN_RANGE = 4
    MOVED_OUT_OWN_RANGE = 5
    HP_ZERO = 6
    USER_ACTIVATE = 7