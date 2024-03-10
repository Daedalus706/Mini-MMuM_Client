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
        """ Places a new Character on a Field. Use It only to sett the initial position of the character, 
            as it does not check if the character is already on the map"""
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return False
        if self.map[x][y].character is not None:
            return False
        
        self.map[x][y].character = character
        return True
    
    def get_pos_of(self, character:Character) -> Field|None:
        """Returns the Field the character is standing on. If the character is not on the map, it retund None"""
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.map[x][y].character == character:
                    return self.map[x][y]
        return None
    
    def get_neighbor(self, field:Field, direction:str) -> Field|None:
        x = field.x
        y = field.y

        match direction:
            case 'up':
                y -= 1
            case 'down':
                y += 1
            case 'left':
                x -= 1
            case 'right':
                x += 1
            case _:
                print("Warning: Invalid direction argument in Map.move(character, direction)")
                return None
        
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return None
        
        return self.map[x][y]

    
    def teleport(self, character:Character, x:int, y:int) -> bool:
        """ Moves a character from one Field to another if possible. It return whether the teleport was successfull or not"""
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return False
        if self.map[x][y].character is not None:
            return False
        
        field = self.get_pos_of(character)
        if field is None:
            return False
        
        field.character = None
        self.map[x][y].character = character

        return True
    
    def move(self, character:Character, direction:str) -> bool:
        """ Moves a charater into a direction. It return whether the move was successfull or not"""
        old_field = self.get_pos_of(character)
        if old_field is None:
            return False
        
        new_field = self.get_neighbor(old_field, direction)

        if new_field is None:
            return False
        
        if new_field.character is not None:
            return False
        
        old_field.character = None
        new_field.character = character

        return True