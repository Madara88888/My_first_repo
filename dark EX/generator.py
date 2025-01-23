import random
import pygame
from settings import *

class gen:
    def __init__(self, WIDTH, HEIGHT):
        self.x = WIDTH
        self.y = HEIGHT
        self.board = []
        void_cell = []
        (
            '\n'.join((self.y - 1) * ([''.join(["." if x % 2 else "#" for x in range(0, (2 * self.x + 1))])[:-1] + "#"] + 
                                                                                  ["#" + ''.join(["." if x % 2 else "#" for x in range(2, (2 * self.x + 1))]) + "#"]))
                                                                                  ) + "\n" + (self.x * 2 + 1) * "#"
        
        for i in range(self.y):
            self.board.append(((self.x * 2 + 1) * "#"))
            self.board.append((''.join(["." if x % 2 else "#" for x in range(0, (2 * self.x + 1))])[:-1] + "#"))
        self.board.append(((self.x * 2 + 1) * "#"))
        
        for  x in range(size_lvl + 1):
            for y in range(size_lvl + 1):
                symbol = self.board[x][y]
                if symbol == "#":
                    p = 0
                if symbol == ".":
                    void_cell.append((y, x))
        
        
        gen_cell = random.choice(void_cell)
        q = 2
        
        
        while void_cell != []:
            right = (gen_cell[0], gen_cell[1] + q)
            left = (gen_cell[0], gen_cell[1] - q)
            top = (gen_cell[0] - q, gen_cell[1])
            bottom = (gen_cell[0] + q, gen_cell[1])
            rand_move = random.choice((right, left, top, bottom))
            if (40 < rand_move[0] < 1) or (40 < rand_move[1] < 1):
                continue
            if self.board[rand_move[0]][rand_move[1]] == ".":
                if rand_move == right:
                    del_cell = self.board.pop(self.board[rand_move[0]][rand_move[1]])
                gen_cell = rand_move
                
                
                print(0)

gen(size_lvl // 2, size_lvl // 2)

        # self.my_file = open("lvl/1.txt", "w+")
        # self.my_file.write('\n'.join(self.board))
        # self.my_file.close()

# RES = WIDTH, HEIGHT = 800, 800
# TILE = 50
# cols, rows = WIDTH // TILE, HEIGHT // TILE

# pygame.init()
# sc = pygame.display.set_mode(RES)
# clock = pygame.time.Clock()


# class Cell:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#         self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
#         self.visited = False

#     def draw_current_cell(self):
#         x, y = self.x * TILE, self.y * TILE
#         pygame.draw.rect(sc, pygame.Color('saddlebrown'), (x + 2, y + 2, TILE - 2, TILE - 2))

#     def draw(self):
#         x, y = self.x * TILE, self.y * TILE
#         if self.visited:
#             pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))

#         if self.walls['top']:
#             pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 3)
#         if self.walls['right']:
#             pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 3)
#         if self.walls['bottom']:
#             pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), 3)
#         if self.walls['left']:
#             pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 3)

#     def check_cell(self, x, y):
#         find_index = lambda x, y: x + y * cols
#         if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
#             return False
#         return grid_cells[find_index(x, y)]

#     def check_neighbors(self):
#         neighbors = []
#         top = self.check_cell(self.x, self.y - 1)
#         right = self.check_cell(self.x + 1, self.y)
#         bottom = self.check_cell(self.x, self.y + 1)
#         left = self.check_cell(self.x - 1, self.y)
#         if top and not top.visited:
#             neighbors.append(top)
#         if right and not right.visited:
#             neighbors.append(right)
#         if bottom and not bottom.visited:
#             neighbors.append(bottom)
#         if left and not left.visited:
#             neighbors.append(left)
#         return choice(neighbors) if neighbors else False


# def remove_walls(current, next):
#     dx = current.x - next.x
#     if dx == 1:
#         current.walls['left'] = False
#         next.walls['right'] = False
#     elif dx == -1:
#         current.walls['right'] = False
#         next.walls['left'] = False
#     dy = current.y - next.y
#     if dy == 1:
#         current.walls['top'] = False
#         next.walls['bottom'] = False
#     elif dy == -1:
#         current.walls['bottom'] = False
#         next.walls['top'] = False


# grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
# current_cell = grid_cells[0]
# stack = []
# colors, color = [], 40

# while True:
#     sc.fill(pygame.Color('darkslategray'))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     [cell.draw() for cell in grid_cells]
#     current_cell.visited = True
#     current_cell.draw_current_cell()
#     [pygame.draw.rect(sc, colors[i], (cell.x * TILE + 2, cell.y * TILE + 2,
#                                          TILE - 4, TILE - 4)) for i, cell in enumerate(stack)]

#     next_cell = current_cell.check_neighbors()
#     if next_cell:
#         next_cell.visited = True
#         stack.append(current_cell)
#         colors.append((min(color, 255), 10, 100))
#         color += 1
#         remove_walls(current_cell, next_cell)
#         current_cell = next_cell
#     elif stack:
#         current_cell = stack.pop()

#     pygame.display.flip()
#     clock.tick(30)