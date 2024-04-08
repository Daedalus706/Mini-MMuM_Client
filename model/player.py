from model.character import Character
from model.team import TEAM


class Player(Character):
    def __init__(self, user_name:str, name: str, user: str, team: TEAM) -> None:
        super().__init__(name, user, team, player=True)
        self.user_name = user_name