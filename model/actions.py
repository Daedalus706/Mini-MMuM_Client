from .map import Map
from .character import Character
from .field import Field

from .area_of_effect import AOE



def weapon_attack(map:Map, user:Character, target_field:Field, aoe_type:AOE, range:int) -> bool:
    """simple weapon attack"""
    user_pos = map.get_pos_of(user)
    if not map.field_in_range(user_pos, target_field, range):
        return False




actions = {
    'weapon_attack': weapon_attack,
}