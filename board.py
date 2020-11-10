#!/usr/bin/env python3

from figures import *
import numpy as np

class Board:
    def __init__(self, size = 8):
        self.size = size
        self.white_figures = [] 
        self.black_figures = []
        self.matrix = np.zeros((size, size), dtype=int)
        self.tmp = np.zeros((size, size), dtype=int)


    def add_figure(self, new_figure):
#        x = new_figure.position[0]
#        y = new_figure.position[1]
        if new_figure.color.name == 'white':
            self.white_figures.append(new_figure)
#            self.matrix[x][y] = Color.white.value
        else:
            self.black_figures.append(new_figure)
#            self.matrix[x][y] = Color.black.value


    def apply_net(self, color):
        self.clear_net()
        if color == Color.white.name:
            for i in self.black_figures:
                self.tmp[i.position[0]][i.position[1]] = Color.black.value
                self.matrix[i.position[0]][i.position[1]] = Color.black.value
            for j in self.white_figures:
                self.matrix[j.position[0]][j.position[1]] = Color.white.value
                self.tmp[j.position[0]][j.position[1]] = Color.white.value
                avail_moves, captures = j.possible_moves(self.matrix)
                for k in avail_moves:
                    self.tmp[k[0]][k[1]] = Color.white.value
                for l in captures:
                    self.tmp[l[0]][l[1]] = Color.white.value
        else:
            for i in self.white_figures:
                self.tmp[i.position[0]][i.position[1]] = Color.white.value
                self.matrix[i.position[0]][i.position[1]] = Color.white.value
            for j in self.black_figures:
                self.tmp[j.position[0]][j.position[1]] = Color.black.value
                self.matrix[j.position[0]][j.position[1]] = Color.black.value
                avail_moves, captures = j.possible_moves(self.matrix)
                for k in avail_moves:
                    self.tmp[k[0]][k[1]] = Color.black.value
                for l in captures:
                    self.tmp[l[0]][l[1]] = Color.black.value

    def apply_figs(self):
        self.clear_matrix()
        for i in self.white_figures:
            self.matrix[i.position[0]][i.position[1]] = Color.white.value
        for j in self.black_figures:
            self.matrix[j.position[0]][j.position[1]] = Color.black.value

    def clear_matrix(self):
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def clear_net(self):
        self.tmp = np.zeros((self.size, self.size), dtype=int)
        self.matrix = np.zeros((self.size, self.size), dtype=int)


    def print_matrix(self):
        print(self.matrix)


#    def remove_figure(self, removed_figure):
