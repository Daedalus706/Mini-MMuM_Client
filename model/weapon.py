from .area_of_effect import AOE


class Weapon:
    def __init__(self, name:str, range:int, one_handed:bool, damage:str, uses:int, aoe_type:AOE, tags:dict) -> None:
        self.name:str = name
        self.range:int = range
        self.one_handed:bool = one_handed
        self.damage:str = damage
        self.uses:int = uses
        self.aoe_type:AOE = aoe_type
        self.tags:dict = tags

        self.uses_left:int = uses

    def use(self):
        self.uses_left -= 1

    def __repr__(self) -> str:
        return f"Weapon({self.name}, one_handed={self.one_handed}, damage={self.damage}, range={self.range}, uses={self.uses}, aoe={self.aoe_type}"