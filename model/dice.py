from enum import Enum

class DICE(Enum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20

    def get_by_string(value:str):
        pos = value.find('D')
        if value[pos+1] == '1' or value[pos+1] == '2':
            s = value[pos:pos+3]
        else:
            s = value[pos:pos+2]