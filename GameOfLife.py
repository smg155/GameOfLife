# Game of life program in Python 3
import pygame
import random
import time

class Cell(object):

    '''
    Addition values for neighboring cells of a current cell.
    '''
    NEIGHBORING_CELLS = [[-1,-1], [0, -1], [1, -1],
                         [-1, 0], [0, 0], [1, 0],
                         [-1, 1], [0, 1], [1, 1]]
    
    def __init__(self, amount, state):
        '''
        Constructor for the board cell objects. Initializes each
        cell to have a state value (either 0 or 1) to represent
        alive or dead, and an amount of living neighbors value
        to represent how many neighbors of the cell are living.
        '''
        self.cell_state = state
        self.amount_living_neighbors = amount
                 
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
                self.grid[b][a] = Cell(0, random.randint(0, 1))

    def update(self):
