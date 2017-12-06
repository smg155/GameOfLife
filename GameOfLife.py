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
        size values to 100.
        '''
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

    def play_game():
        '''
        The method to play the game.
        '''

if __name__ == "__main__":
    play_game()
