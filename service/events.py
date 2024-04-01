from enum import Enum
from model import Character, DICE


class EventType(Enum):
    NEW_CHARACTER = 0
    ROLL_DICE = 1


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
