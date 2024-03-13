from enum import Enum

class TRIGGER(Enum):
    NONE = 0
    MATCH_START = 1
    ROUND_START = 2
    ROUND_END = 3
    MOVED_IN_OWN_RANGE_CLOSE = 4
    MOVED_IN_OWN_RANGE_EXTENDED = 5
    MOVED_IN_OWN_RANGE_RANGED = 6
    MOVED_OUT_OWN_RANGE_CLOSE = 7
    MOVED_OUT_OWN_RANGE_EXTENDED = 8
    MOVED_OUT_OWN_RANGE_RANGED = 9
    HP_ZERO = 10
    USER_ACTIVATE = 11

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
                return TRIGGER.MOVED_IN_OWN_RANGE_CLOSE
            case 5:
                return TRIGGER.MOVED_IN_OWN_RANGE_EXTENDED
            case 6:
                return TRIGGER.MOVED_IN_OWN_RANGE_RANGED
            case 7:
                return TRIGGER.MOVED_OUT_OWN_RANGE_CLOSE
            case 8:
                return TRIGGER.MOVED_OUT_OWN_RANGE_EXTENDED
            case 9:
                return TRIGGER.MOVED_OUT_OWN_RANGE_RANGED
            case 10:
                return TRIGGER.HP_ZERO
            case 11:
                return TRIGGER.USER_ACTIVATE
            case _:
                raise ValueError(f"Invalid argument for value: {value}")
            
if __name__ == '__main__':
    print(TRIGGER.get_by_value(4))
    print(TRIGGER.get_by_value(7))