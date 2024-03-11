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
        self.base_bonus_actions:int = 1

        self.hp:int = self.base_hp
        self.ac:int = self.base_ac
        self.moves:int = self.base_moves
        self.actions:int = self.base_actions
        self.bonus_actions:int = self.base_bonus_actions

    def new_round(self):
        self.actions = self.base_actions
        self.bonus_actions = self.base_bonus_actions
        self.moves = self.base_moves

    def get_hp(self) -> int:
        return self.hp

    def get_ac(self) -> int:
        if self.armor is None:
            return self.ac
        return self.ac + self.armor.ac
    
    def get_actions(self) -> int:
        return self.actions
    
    def get_bonus_actions(self) -> int:
        return self.base_bonus_actions
    
    def get_moves(self) -> int:
        return self.moves