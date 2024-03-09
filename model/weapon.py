class Weapon:
    def __init__(self, name:str, uses:int, range:int) -> None:
        self.name:str = name
        self.uses:int = uses
        self.range:int = range

        self.uses_left:int = uses

    def use(self):
        self.uses_left -= 1