from model import Map, Field

if __name__ == "__main__":
    for i in range(6):
        for y in range(-6, 7):
            s = ""
            for x in range(-6, 7):
                if Map.field_in_range(None, (0, 0), Field(x, y), i):
                    s += ' #'
                else:
                    s += '  '
            print(s)