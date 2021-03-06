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
        all_figures = self.black_figures + self.white_figures
        for fig in all_figures:
            if fig.position != [-1, -1]:
                x = fig.position[0]
                y = fig.position[1]
                self.tmp[x][y] = fig.color.value
                self.matrix[x][y] = fig.color.value
        if color == 'white':
            ref_fig = self.white_figures
        else: 
            ref_fig = self.black_figures
        for fig in ref_fig:
            if fig.position != [-1, -1]:
                avail_moves, captures = fig.possible_moves(self.matrix)
                for k in avail_moves:
                    self.tmp[k[0]][k[1]] = fig.color.value
                for l in captures:
                    self.tmp[l[0]][l[1]] = fig.color.value

    def apply_figs(self):
        self.clear_matrix()
        all_figures = self.white_figures + self.black_figures
        for fig in all_figures:
            if fig.position != [-1, -1]:
                self.matrix[fig.position[0]][fig.position[1]] = fig.color.value

    def clear_matrix(self):
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def clear_net(self):
        self.clear_matrix()
        self.tmp = np.zeros((self.size, self.size), dtype=int)

