# Game of life program in Python 3
import pygame
import random
import time

class Cell(object):
    
    def __init__(self, position, state):
        '''
        Constructor for the board cell objects. Initializes each
        cell to have a state value (either 0 or 1) to represent
        alive or dead, and an amount of living neighbors value
        to represent how many neighbors of the cell are living.
        '''
        self.cell_state = state
                 
class GameBoard(object):

    def __init__(self, screen, size_x, size_y, time, game_state=None):
        '''
        Constructor for the board object. Initializes
        a 2D array integers with the default value of zero
        for the specified size of the game board. If the size
        values for the board are greater than 100, sets the
        size values to 100. Does the same with time.
        '''
        self.width = size_x
        self.height = size_y
        if size_x > 100:
            size_x = 100
        if size_y > 100:
            size_y = 100
        if time > 100: #Not sure about this part exactly...
            time = 100 #Definitely have to research the time package
        self.grid = [[x for x in range(size_x)] for x in range(size_y)]
        if game_state is not None:
            self.grid = game_state
        for a in range(size_x):
            for b in range(size_y):
                self.grid[b][a] = Cell(random.randint(0, 1))

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
        next_state = list(self.grid)
        for i in range(self.width):
            for j in range(self.height):
                count = adjacent(i, j)
                if count > 3:
                    next_state[j][i] = 0
                elif count < 2:
                    next_state[j][i] = 0
                elif count == 3:
                    next_state[j][i] = 1
                else:
                    next_state[j][i] = self.grid[j][i]
        self.grid = next_state
        return self.grid


    def adjacent(self, x, y):
        '''
        Counts the number of filled values are adjacent to the point.
        '''
        count = 0
        for i in range(x - 1, x + 1):
            for j in range(y - 1, y + 1):
                if i != x or j != y:
                    count += self.grid[(i + self.width) % self.width] \
                             [(j + self.height) % self.width]
        return count

def text_format(message, x, y):
    screen = pygame.display.set_mode((x, y))
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(message), True, (255, 160, 122))
    return screen.blit(text, (x, y))

def asking(message):
    user_input = 0
    text_format(message, 300, 400)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_1:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_2:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_3:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_4:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_5:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_6:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_7:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_8:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_9:
                    user_input += int(chr(event.key))
                if event.key == pygame.K_RETURN:
                    user_input = True
    return user_input

def game_introduction():
    intro = True
    nums = [0] * 3
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
    return nums

def play_game():
    '''
    The method to play the game.
    '''
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    background = pygame.Surface((500, 500))
    background.fill((0, 0, 0))
    numbers = game_introduction()
    pygame.display.update()
    board = GameBoard(screen, numbers[0], numbers[1], numbers[2], None)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        for r in range(numbers[0]):
            for c in range(numbers[0]):
                if grid[r][c].state == 1:
                    pygame.draw.rect(background, (255, 255, 255), (r*10, c*10, 10, 10))
                else:
                    pygame.draw.rect(background, (0, 0, 0), (r*10, c*10, 10, 10))
        board.update()
        screen.blit(background, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
	play_game()
