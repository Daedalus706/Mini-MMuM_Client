from .character import Character


class Field:
    def __init__(self, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y

        self.character:Character = None
    
    def get_pos(self) -> tuple[int,int]:
        return (self.x, self.y)