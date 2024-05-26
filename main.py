"""

Main File for sudoku handling main logic

"""
import pygame 
import time

pygame.init()

WIDTH, HEIGHT = 540, 540
ROWS,COLS = 9,9
CELL_SIZE = WIDTH//COLS

class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.dictionary = {0:' ',1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:'8',9:'9'}
    def find_next_empty(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    return row, col
        return None, None

    def is_valid(self,guess,row,col):
        r_value = self.puzzle[row]
        if guess in r_value: return False
        
        for i in range(9): 
            if guess == self.puzzle[i][col]: return False

        row_start = (row//3) * 3
        col_start = (col//3) * 3

        for r in range(row_start, row_start +3):
            for c in range(col_start, col_start+3):
                if guess == self.puzzle[r][c]:
                    return False
        return True

    def solve_sudoku(self,screen):
        row,col = self.find_next_empty()

        if row is None:
            return True
        
        for guess in range(1,10):
            if self.is_valid(guess,row,col):
                self.puzzle[row][col] = guess
                self.update_display(screen)
                if self.solve_sudoku(screen):
                    return True
                self.puzzle[row][col] = 0
                self.update_display(screen)
        
        return False
    
    def terminal_print(self):
        for i in range(9):
            for j in range(9):
                print(self.puzzle[i][j],end=" ")
            print()
            
    def update_display(self,screen):
        draw_grid(screen)
        draw_numbers(self.puzzle,self.dictionary)
        pygame.display.flip()
        time.sleep(0.1)

def draw_grid(screen):
    for row in range(9):
        for col in range(9):
            box = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(255,255,255),box)
            pygame.draw.rect(screen,(0,0,0),box,1)

def draw_numbers(puzzle,dictionary):
    for row in range(9):
        for col in range(9):
            txt = dictionary[puzzle[row][col]]
            img = font.render(txt, True, pygame.Color((0,0,0)),
                  pygame.Color((255,255,255)))
            screen.blit(img, (col*CELL_SIZE + 30,row*CELL_SIZE + 15))
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

board = Sudoku(grid)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('Arial',16, bold = True)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("black")

    board.solve_sudoku(screen)