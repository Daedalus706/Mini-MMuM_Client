from model import *

class GameService:
    def __init__(self, field_size:tuple[int, int]) -> None:
        self.map = Map(field_size)

        self.caracters:list[Character] = []
        self.players:list[Character] = []

    def handle_data(self, data:dict) -> None:
        if data != None:
            print(data)

        


    

