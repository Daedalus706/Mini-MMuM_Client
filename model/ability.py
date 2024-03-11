from .trigger import TRIGGER


class Ability:
    def __init__(self, name:str, active:bool, triggers:list[TRIGGER], tags:list) -> None:
        self.name:str = name
        self.active:bool = active
        self.triggers:list[TRIGGER] = triggers
        self.tags:list = tags