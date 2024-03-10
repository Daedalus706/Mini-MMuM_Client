from .character import Character

from .field import Field

class Map:
    def __init__(self, size:tuple[int, int]) -> None:

        self.map:list[list[Field]] = []
        self.size:tuple[int, int] = size

        for x in range(size[0]):
            self.map.append([])
            for y in range(size[1]):
                self.map[x].append(Field(x, y))

    def place(self, character:Character, x:int, y:int) -> bool:
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return False
        if self.map[x][y].character is not None:
            return False
        
        self.map[x][y].character = character
        return True
    