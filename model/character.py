from .armor import Armor
from .weapon import Weapon

class Character:
    def __init__(self, name:str) -> None:
        self.name:str = name
        self.armor:Armor = None

        self.base_hp:int = 50
        self.base_ac:int = 4
        self.base_moves:int = 3
        self.base_actions:int = 2

        self.hp:int = self.base_hp
        self.ac:int = self.base_ac
        self.moves:int = self.base_moves
        self.actions:int = self.base_actions

    def new_round(self):
        self.actions = self.base_actions
        self.moves = self.base_moves

    def get_ac(self):
        return self.ac + self.armor.ac