from .character import Character
from .field import Field
from .area_of_effect import AOE

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
    
    def get_at(self, x:int, y:int) -> Field|None:
        """Get the Field at the provided position, if possible"""
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return None
        return self.map[x][y]
    
    def get_character_at(self, x:int, y:int) -> Field|None:
        """Get the Character at the provided position, if possible"""
        if not 0 <= x < self.size[0] or not 0 <= y < self.size[1]:
            return None
        return self.map[x][y].character
    
    
    def get_pos_of(self, character:Character) -> Field|None:
        """Returns the Field the character is standing on. If the character is not on the map, it retund None"""
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.map[x][y].character == character:
                    return self.map[x][y]
        return None
    
    def get_neighbor(self, field:Field, direction:str) -> Field|None:
        """Get the neighboring Field in the provided direction"""
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
        
        return self.get_at(x, y)

    
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
        if not character.can_move():
            return False

        old_field = self.get_pos_of(character)
        if old_field is None:
            return False
        
        new_field:Field = self.get_neighbor(old_field, direction)

        if new_field is None:
            return False
        
        if new_field.character is not None:
            return False
        
        old_field.character = None
        new_field.character = character

        character.move()

        return True
    
    def get_in_area(self, pos:tuple[int,int], area:AOE, orientation:str='horizontal') -> set[Character]:
        """Gett all characters in the area of an AOE effect"""
        in_area = set()
        if area == AOE.LINE:
            fields = AOE.FIELDS[AOE.LINE][orientation]
        else:
            fields = AOE.FIELDS[area]

        for field in fields:
            character = self.get_character_at(pos[0] + field[0], pos[1] + field[1])
            if character is not None:
                in_area.add(character)

    def get_in_range(self, pos:tuple[int,int], value:int) -> set[Character]:
        """Get a set of characters in the attack range of the provided poition"""
        in_range = set()
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        for r in range(1, value):
                
            for direction in directions:
                for off in range(-1, 2):
                    if direction[0] == 0:
                        off_x = off
                        off_y = 0
                        if off == 0:
                            off_y = direction[1]
                    else:
                        off_x = 0
                        off_y = off
                        if off == 0:
                            off_x = direction[0]

                    x = pos[0] + off_x + r * direction[0]
                    y = pos[0] + off_y + r * direction[1]
                    if self.map[x][y].character is not None:
                        in_range.add(self.get_at(x, y))

        in_range.add(self.get_character_at(pos[0]+1, 0).character)
        in_range.add(self.get_character_at(pos[0]-1, 0).character)
        in_range.add(self.get_character_at(0, pos[1]+1).character)
        in_range.add(self.get_character_at(0, pos[1]-1).character)

        if None in in_range:
            in_range.remove(None)

        return in_range

    def field_in_range(self, pos:tuple[int,int], target:Field, value:int):
        """Checks if the target is in range of the provided origin pos coordinate"""
        pos2 = target.get_pos()
        
        rel_pos = (pos[0] - pos2[0], pos[1] - pos2[1])
        if abs(rel_pos[0]) > 1 and abs(rel_pos[1]) > 1:
            return False
        
        if abs(rel_pos[0]) + abs(rel_pos[1]) <= value:
            return True
        
        return False

