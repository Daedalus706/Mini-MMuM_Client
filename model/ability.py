from .trigger import TRIGGER


class Ability:
    def __init__(self, name:str, range:int, cost:int, active:bool, bonus:bool, action:str, action_queue:list, tags:dict, triggers:list[TRIGGER]=None) -> None:
        self.name:str = name
        self.range:int = range
        self.cost:int = cost
        self.active:bool = active
        self.bonus:bool = bonus
        self.action:str = action
        self.tags:dict = tags
        self.action_queue:list = action_queue
        self.triggers:list[TRIGGER] = triggers

    def __repr__(self) -> str:
        return f"Ability('{self.name}', range={self.range}, cost={self.cost}, active={self.active}, bonus={self.bonus}, tags={self.tags})"
    