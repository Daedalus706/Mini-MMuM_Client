from model import *

class GameService:
    def __init__(self, field_size:tuple[int, int]) -> None:
        self.map = Map(field_size)

        self.characters:list[Character] = []
        self.players:dict[str:Character] = {}

    def handle_data(self, data:dict[str:str]) -> None:
        if data != None:

            if not 'userName' in data:
                return
            else:
                if not data['userName'] in self.players:
                    new_character = Character(f"{data['userName']}'s character")
                    self.players[data['userName']] = new_character
                    self.characters.append(new_character)
                    for x in range(10):
                        if self.map.place(new_character, x, 0):
                            break
            
            if 'move' in data:
                character:Character = self.players[data['userName']]
                print('moved', character.name)


    

