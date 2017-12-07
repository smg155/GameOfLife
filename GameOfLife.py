# Game of life program in Python 3
import pygame
import random
import time

class Cell(object):
    
    def __init__(self, state):
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
        next_state = list(grid)
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

    def play_game():
        '''
        The method to play the game.
        '''
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        background = pygame.Surface((600, 600))
        background.fill(black)
        '''
        Ask for a board size and a run time.
        Clearly have to do this before anything can work.
        Probably want to have a pop up box ask this and
        have the user input their answers and what not.
        '''
        board = GameBoard(screen, '''size_x''', '''size_y''', '''Time''', None)
        while True:
            #Play da game ya
            

if __name__ == "__main__":
    play_game()
