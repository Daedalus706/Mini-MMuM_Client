from enum import Enum
from model import Character


class EventType(Enum):
    NEW_CHARACTER = 0


class Event:

    class NewChraracter():
        def __init__(self, character:Character) -> None:
            self.character:Character = character
            self.type:EventType = EventType.NEW_CHARACTER
