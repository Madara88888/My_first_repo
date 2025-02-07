from settings import *
from generator import *

class Lvl:
    pass

def load_lvl(number) -> Lvl:
    lvlname = f"lvl/{number}.txt"
    lvl = [["." for k in range(size_lvl + 1)] for i in range(size_lvl + 1)]
    with open(lvlname) as file:
        
        for line, y in zip(file.readlines(), range(size_lvl + 1)):
            for symbol, x in zip(line.rstrip(), range(len(line.rstrip()))):
                if symbol == "#":
                    lvl[y][x] = "#"
                if symbol == "&":
                    lvl[y][x] = "&"
                if symbol == "@":
                    lvl[y][x] = "."
                    player_pos = (x * CELL + CELL // 2, y * CELL + CELL // 2)

    return player_pos, lvl


