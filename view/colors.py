class Color:
    GOLD = 0xb9a158
    BROWN = 0x6e4930
    COPPER = 0xb16a3b
    LIGHT_BLUE = 0x5060a0

    def to_tuple(color:int) -> tuple[int, int, int]:
        r = color//(256*256)
        g = color//256-r*256
        b = color%256
        return (r, g, b)