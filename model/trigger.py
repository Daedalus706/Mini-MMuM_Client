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

    def get_by_value(value:int):
        match value:
            case 0:
                return TRIGGER.NONE
            case 1:
                return TRIGGER.MATCH_START
            case 2:
                return TRIGGER.ROUND_START
            case 3:
                return TRIGGER.ROUND_END
            case 4:
                return TRIGGER.MOVED_IN_OWN_RANGE
            case 5:
                return TRIGGER.MOVED_OUT_OWN_RANGE
            case 6:
                return TRIGGER.USER_ACTIVATE
            case _:
                raise ValueError(f"Invalid argument for value: {value}")
            
if __name__ == '__main__':
    print(TRIGGER.get_by_value(4))
    print(TRIGGER.get_by_value(7))