import random

class gen:
    def __init__(self, lvl):
        if int(lvl) == 1:
            self.x = 8
            self.y = 8
            self.road = 1
            self.board = (self.y - 1) * ("\n".join((("#" * 20 * self.x) + ',' + 19 * (''.join(["".join(list("#" + ("-" * 19))) for _ in range(8)])[:-1] + "#" + ',')).split(","))) + ("\n".join((("#" * 20 * self.x) + ',' + 18 * (''.join(["".join(list("#" + ("-" * 19))) for _ in range(8)])[:-1] + "#" + ',')).split(","))) + ("#" * 20 * self.x)
            my_file = open("lvl/1.txt", "w+")
            my_file.write(self.board)
            my_file.close()

gen(1)