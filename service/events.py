from enum import Enum
from model import Character, DICE


class EventType(Enum):
    NEW_CHARACTER = 0
    ROLL_DICE = 1
    READY_TO_ROLL = 2
    AC_HIT = 3
    AC_MISS = 4
    


class Event:

    class NewChraracter():
        def __init__(self, character:Character) -> None:
            self.type:EventType = EventType.NEW_CHARACTER
            self.character:Character = character
    
    class RollDice():
        def __init__(self, dice:DICE, number:int) -> None:
            self.type:EventType = EventType.ROLL_DICE
            self.dice:DICE = dice
            self.number:int = number
    
    class ReadyToRoll():
        def __init__(self, dice:DICE) -> None:
            self.type:EventType = EventType.READY_TO_ROLL
            self.dice:DICE = dice
    
    class AcHit():
        def __init__(self, crit:bool=False) -> None:
            self.type:EventType = EventType.AC_HIT
            self.crit:bool = crit

    class AcMiss():
        def __init__(self, crit:bool=False) -> None:
            self.type:EventType = EventType.AC_MISS
            self.crit:bool = crit
    
    