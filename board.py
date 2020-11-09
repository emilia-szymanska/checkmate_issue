#!/usr/bin/env python3

from figures import *
import numpy as np

class Board:
    def __init__(self, size = 8):
        self.size = size
        self.white_figures = [] 
        self.black_figures = []
        self.matrix = np.zeros((size, size), dtype=int)


    def add_figure(self, new_figure):
        x = new_figure.position[0]
        y = new_figure.position[1]
        if new_figure.color.name == 'white':
            self.white_figures.append(new_figure)
            self.matrix[x][y] = Color.white.value
        else:
            self.black_figures.append(new_figure)
            self.matrix[x][y] = Color.black.value


    def print_matrix(self):
        print(self.matrix)
        #for i in range(self.size):
        #    print(self.matrix[i])
