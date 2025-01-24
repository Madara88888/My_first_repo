import random
from settings import *

class gen:
    def __init__(self, WIDTH, HEIGHT):
        self.x = WIDTH
        self.y = HEIGHT
        self.board = []
        void_cell = []
        
        for i in range(self.y):
            self.board.append(list((self.x * 2 + 1) * "#"))
            self.board.append(list(''.join(["." if x % 2 else "#" for x in range(0, (2 * self.x + 1))])[:-1] + "#"))
        self.board.append(list((self.x * 2 + 1) * "#"))
        
        for  x in range(size_lvl + 1):
            for y in range(size_lvl + 1):
                symbol = self.board[x][y]
                if symbol == ".":
                    void_cell.append((y, x))
        

        start_cell = random.choice(void_cell)
        q = 2
        count = 0
        gen_cell = [start_cell]
        while void_cell != []:
            
            
            for i in gen_cell:
                right = (i[0], i[1] + q)
                left = (i[0], i[1] - q)
                top = (i[0] - q, i[1])
                bottom = (i[0] + q, i[1])
                rand_move = random.choice((right, left, top, bottom))
                if rand_move in void_cell:
                    if self.board[rand_move[0]][rand_move[1]] == ".":
                        if right == rand_move:
                            # print(f"#{(rand_move[0], rand_move[1] + 1)}#", "=>", right, f"(*{rand_move}*)")
                            self.board[rand_move[0]][rand_move[1] - 1] = "."
                            void_cell.remove(rand_move)
                            count = 0
                        elif left == rand_move:
                            # print(f"#{(rand_move[0], rand_move[1] - 1)}#", "<=", left, f"(*{rand_move}*)")
                            self.board[rand_move[0]][rand_move[1] + 1] = "."
                            void_cell.remove(rand_move)
                            count = 0
                        elif top == rand_move:
                            # print(f"#{(rand_move[0] + 1, rand_move[1])}#", "./\.", top, f"(*{rand_move}*)")
                            self.board[rand_move[0] + 1][rand_move[1]] = "."
                            void_cell.remove(rand_move)
                            count = 0
                        elif bottom == rand_move:
                            # print(f"#{(rand_move[0] - 1, rand_move[1])}#", "VV", bottom, f"(*{rand_move}*)")
                            self.board[rand_move[0] - 1][rand_move[1]] = "."
                            void_cell.remove(rand_move)
                            count = 0
                        else:
                            count += 1
                        gen_cell.append(rand_move)

            if count == len(gen_cell):
                break
        
        list_map = []
        for i in self.board:
            list_map.append(''.join(i))
        # print("\n".join(list_map))
        # print(void_cell)

        self.my_file = open("lvl/1.txt", "w+")
        self.my_file.write('\n'.join(list_map))
        self.my_file.close()

gen(size_lvl // 2, size_lvl // 2)

