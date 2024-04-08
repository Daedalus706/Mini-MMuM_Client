from model.character import Character
from model.team import TEAM


class NPC(Character):
    def __init__(self, name: str, user: str, team: TEAM) -> None:
        super().__init__(name, user, team, player=False)