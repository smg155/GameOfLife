# Game of life program in Python 3
import pygame
from pygame.locals import *
import random
import time

##################################################
'''
GameBoard Class.
'''

class GameBoard(object):

    def __init__(self, screen, size_x, size_y, time, random_or_not, game_state=None):
        '''
        Constructor for the board object. Initializes
        a 2D array integers with the default value of zero
        for the specified size of the game board. If the size
        values for the board are greater than 100, sets the
        size values to 100. Does the same with time.
        '''
        self.width = size_x
        self.height = size_y
        self.it = time
        if self.width > 100:
            self.width = 100
        if self.height > 100:
            self.height = 100
        if self.it > 1000:
            self.it = 1000
        self.grid = [[0 for x in range(size_x)] for y in range(size_y)]
        if game_state is not None:
            self.grid = game_state
        if random_or_not == 0:
            for a in range(size_x):
                for b in range(size_y):
                    self.grid[b][a] = random.randint(0, 1)
        else:
            for a in range(size_x):
                for b in range(size_y):
                    if a == 2 and b == 1:
                        self.grid[b][a] = 1
                    elif a == 3 and b == 2:
                        self.grid[b][a] = 1
                    elif (a == 1 or a == 2 or a == 3) and b == 3:
                        self.grid[b][a] = 1
                    else:
                        self.grid[b][a] = 0
                    

    def get_grid(self):
        return self.grid

    def get_iterations(self):
        return self.it

    def adjacent(self, x, y):
        '''
        Counts the number of filled values are adjacent to the point.
        '''
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    current_cell = self.grid[(j + self.width) % self.width][(i + self.width) % self.width]
                    count += current_cell
        return count
    
    def update(self):
        '''
        This method is more the backend of the program.
        Basically how we decide how we want to update the
        board. I think it would be best to wrap around the
        board in the shape of torus with finite area but no
        boundary so that patterns can continue even if they
        reach the "edge" of the board. We can do this
        in a relatively simple way and count the neighboring
        cells at the same time.
        '''
        next_state = [[0 for x in range(self.width)] for y in range(self.height)]
        for a in range(self.width):
                for b in range(self.height):
                    next_state[b][a] = self.grid[b][a]
        for i in range(self.width):
            for j in range(self.height):
                count = self.adjacent(i, j)
                if self.grid[j][i] == 1 and 2 <= count <= 3:
                    next_state[j][i] = 1
                else:
                    next_state[j][i] = 0
                if self.grid[j][i] == 0 and count == 3:
                    next_state[j][i] = 1
        self.grid = next_state
        return self.grid

##################################################
'''
Main methods for the game.
'''

def text_format(message, x, y):
    pygame.font.init()
    screen = pygame.display.set_mode((x, y))
    font = pygame.font.SysFont('Arial', 40, bold=True)
    image = font.render(message, True, (255, 160, 120))
    return screen.blit(image, (20, 20))

def asking(message):
    user_input = ''
    text_format(message, 700, 700)
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                else:
                    key = pygame.key.name(event.key)
                    user_input += key                   
    return user_input

def game_introduction():
    intro = True
    nums = [0] * 4
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
            nums[0] = asking("Board width: ")
            nums[1] = asking("Board height: ")
            nums[2] = asking("Number of iterations: ")
            nums[3] = asking("Random or Glider (Type 0 or 1):")
            intro = False
            break
    return nums

def play_game():
    '''
    The method to play the game.
    '''
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    background = pygame.Surface((700, 700))
    background.fill((0, 0, 0))
    numbers = game_introduction()
    pygame.display.update()
    board = GameBoard(screen, int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3]), None)
    grid = board.get_grid()
    i = 0
    while i < board.get_iterations():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        for r in range(int(numbers[0])):
            for c in range(int(numbers[1])):
                if grid[c][r] == 1:
                    pygame.draw.rect(background, (255, 255, 255), (r*10, c*10, 10, 10))
                else:
                    pygame.draw.rect(background, (0, 0, 0), (r*10, c*10, 10, 10))
        grid = board.update()
        screen.blit(background, (0, 0))
        pygame.display.update()
        i += 1
        time.sleep(0.1)
    quit()

if __name__ == '__main__':
	play_game()
