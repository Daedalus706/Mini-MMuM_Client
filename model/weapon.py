from .area_of_effect import AOE


class Weapon:
    def __init__(self, name:str, uses:int, range:int, aoe_type:AOE) -> None:
        self.name:str = name
        self.uses:int = uses
        self.range:int = range
        self.aoe_type:AOE = aoe_type

        self.uses_left:int = uses

    def use(self):
        self.uses_left -= 1