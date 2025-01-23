import pygame
from settings import *
from generator import *

class Lvl:
    pass

def load_lvl(number) -> Lvl:
    lvlname = f"lvl/{number}.txt"
    lvl = [["." for k in range(size_lvl + 1)] for i in range(size_lvl)]
    print(lvl)
    with open(lvlname) as file:
        
        for line, y in zip(file.readlines(), range(size_lvl + 1)):
            for symbol, x in zip(line.rstrip(), range(len(line.rstrip()))):
                if symbol == "#":
                    lvl[y][x] = "#"

                if symbol == "@":
                    player_pos = (x * CELL, y * CELL)
                else:
                    player_pos = (1 * CELL, 1 * CELL)

    return player_pos, lvl

player_pos, lvl = load_lvl(2)
