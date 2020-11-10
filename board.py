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
        self.black_king = King([-1, -1], 'black')
        self.white_king = King([-1, -1], 'white')

    def add_figure(self, new_figure):
        if new_figure.color.name == 'white':
            self.white_figures.append(new_figure)
        else:
            self.black_figures.append(new_figure)

    def move_figure(self, figure, new_pose):
        figure.move(new_pose)
        captured = False
        fig_captured = []
        if figure.color.name == 'white':
            figs = self.black_figures
        else:
            figs = self.white_figures
        
        for fig in figs:
            if fig.position == new_pose:
                fig.remove()
                fig_captured = fig
                captured = True
                break
        
        return captured, fig_captured

    def apply_net(self, color):
        self.clear_net()
        if color == Color.white.name:
            for i in self.black_figures:
                if i.position != [-1, -1]:
                    self.tmp[i.position[0]][i.position[1]] = Color.black.value
                    self.matrix[i.position[0]][i.position[1]] = Color.black.value
            for j in self.white_figures:
                if j.position != [-1, -1]:
                    self.matrix[j.position[0]][j.position[1]] = Color.white.value
                    self.tmp[j.position[0]][j.position[1]] = Color.white.value
                    avail_moves, captures = j.possible_moves(self.matrix)
                    for k in avail_moves:
                        self.tmp[k[0]][k[1]] = Color.white.value
                    for l in captures:
                        self.tmp[l[0]][l[1]] = Color.white.value
        else:
            for i in self.white_figures:
                if i.position != [-1, -1]:
                    self.tmp[i.position[0]][i.position[1]] = Color.white.value
                    self.matrix[i.position[0]][i.position[1]] = Color.white.value
            for j in self.black_figures:
                if j.position != [-1, -1]:
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
            if i.position != [-1, -1]:
                self.matrix[i.position[0]][i.position[1]] = Color.white.value
        for j in self.black_figures:
            if j.position != [-1, -1]:
                self.matrix[j.position[0]][j.position[1]] = Color.black.value

    def clear_matrix(self):
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def clear_net(self):
        self.clear_matrix()
        self.tmp = np.zeros((self.size, self.size), dtype=int)


    def print_matrix(self):
        print(self.matrix)

