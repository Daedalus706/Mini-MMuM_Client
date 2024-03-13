

class AOE:
    SINGLE = 0
    LINE = 1
    AREA = 2
    LARGE_AREA = 3

    FIELDS:dict = {
        SINGLE: ((0, 0),),

        LINE: {
            'horizontal': ((-1, 0), (0, 0), (1, )),
            'vertical': ((0, -1), (0, 0), (0, 1)),
        },

        AREA: ((-1, -1), (0, -1), (1, -1),
               (-1, 0), (0, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)),

        LARGE_AREA:((-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
                    (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                    (-2, 0),  (-1, 0),  (0, 0),  (1, 0),  (2, 0),
                    (-2, 1),  (-1, 1),  (0, 1),  (1, 1),  (2, 1),
                    (-2, 2),  (-1, 2),  (0, 2),  (1, 2),  (2, 2))
    }

    def get_by_value(value:int):
        match value:
            case 0:
                return AOE.SINGLE
            case 1:
                return AOE.LINE
            case 2:
                return AOE.AREA
            case 3:
                return AOE.LARGE_AREA
            case _:
                raise ValueError(f"Invalid argument for value: {value}")

    