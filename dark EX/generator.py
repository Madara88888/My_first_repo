import random
from settings import *

class gen:
    def __init__(self, WIDTH, HEIGHT):
        self.x = WIDTH
        self.y = HEIGHT
        for num_lvl in range(1, QUANTITY_LVLS):
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
            possible_end = []
            start_len = len(void_cell)
            start_pos = (1, 1)
            while void_cell != []:
                
                
                for i in gen_cell:
                    right = (i[0], i[1] + q)
                    left = (i[0], i[1] - q)
                    top = (i[0] - q, i[1])
                    bottom = (i[0] + q, i[1])
                    rand_move = random.choice((right, left, top, bottom))

                    
                    if rand_move in void_cell:
                        if len(void_cell) == start_len:
                            start_pos = start_cell
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

                    if not(void_cell) == False:
                        if len(void_cell) == 1:
                            possible_end.append(void_cell[-1])

                if count == len(gen_cell):
                    break
            
            
            # print(num_lvl, start_pos[1], possible_end[-1][1], abs(int(start_pos[1]) - int(possible_end[-1][1])) < ((size_lvl // 2) - 1), "y")
            # print(num_lvl, start_pos[0], possible_end[-1][0], abs(int(start_pos[0]) - int(possible_end[-1][0])) < ((size_lvl // 2) - 1), "x")
            count = 0
            while (abs(int(start_pos[0]) - int(possible_end[-1][0])) < ((size_lvl // 2) - 1)
                   ) or (abs(int(start_pos[1]) - int(possible_end[-1][1])) < ((size_lvl // 2) - 1)):

                if (abs(int(start_pos[0]) - int(possible_end[-1][0])) >= ((size_lvl // 2) - 1)
                    ) and (abs(int(start_pos[1]) - int(possible_end[-1][1])) >= ((size_lvl // 2) - 1)):
                    break

                if count == ((size_lvl ** 2) // 2):
                    start_pos = random.choice(((3, 3), (size_lvl - 3, 3), (3, size_lvl - 3), (size_lvl - 3, size_lvl - 3)))
                    break

                right = (start_pos[0], start_pos[1] + q)
                left = (start_pos[0], start_pos[1] - q)
                top = (start_pos[0] - q, start_pos[1])
                bottom = (start_pos[0] + q, start_pos[1])
                rand_move = random.choice((right, left, top, bottom))
                start_pos = rand_move

                if not((0 < start_pos[0] < size_lvl) and (0 < start_pos[1] < size_lvl)):
                    start_pos = random.choice(((3, 3), (size_lvl - 3, 3), (3, size_lvl - 3), (size_lvl - 3, size_lvl - 3)))
                
                count += 1
            

            self.board[start_pos[0]][start_pos[1]] = "@"
            self.board[possible_end[-1][0]][possible_end[-1][1]] = "&"
            list_map = []
            for i in self.board:
                list_map.append(''.join(i))
            # print("\n".join(list_map))
            # print(void_cell)
            

            self.my_file = open(f"lvl/{num_lvl}.txt", "w+")
            self.my_file.write('\n'.join(list_map))
            self.my_file.close()

gen(size_lvl // 2, size_lvl // 2)

