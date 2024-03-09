from .character import Character

from .field import Field

class Map:
    def __init__(self, size:tuple[int, int]) -> None:

        self.map:list[list[Field]] = []
        self.size:tuple[int, int] = size

        for y in range(size[1]):
            self.map.append([])
            for x in range(size[0]):
                self.map[y].append(Field(x, y))