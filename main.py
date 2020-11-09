#!/usr/bin/env python3

from board import *

x = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0], 
    [0, 0, 2, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
    ]


p = Pawn([1, 3], 'black')
board = Board(5)
board.add_figure(p)
#board.matrix[0][0] = 3
board.print_matrix()

#pos, cap = p.possible_moves(x)
#print(pos)
#print(cap)

#print(x[0])
#print(x[1])
#print(x[2])
#print(x[3])
#print(x[4])
