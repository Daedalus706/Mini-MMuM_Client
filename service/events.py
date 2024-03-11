from enum import Enum
from model import Character


class EventType(Enum):
    NEW_CHARACTER = 0


class Event:

    class NewChraracter():
        def __init__(self, character:Character) -> None:
            self.character = character
            self.type = EventType.NEW_CHARACTER
