from .trigger import TRIGGER


class Ability:
    def __init__(self, name:str, active:bool) -> None:
        self.name:str = name
        self.active:bool = active