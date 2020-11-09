#!/usr/bin/env python3

from board import *

SIZE = 8

if __name__ == "__main__":
    
#    x = []
#    for i in range(SIZE):
#        for j in range(SIZE):
#            element = input()
#            x.append(element)
#    print(x)

    
    board = Board(SIZE)

    bp = Pawn([5, 1], 'black')
    wp = Pawn([6, 7], 'white')
    bW = King([0, 2], 'black')
    wW = King([7, 4], 'white')
    wr = Rook([1, 4], 'white')
    wq = Queen([3, 3], 'white')
    board.add_figure(bp)
    board.add_figure(wp)
    board.add_figure(bW)
    board.add_figure(wW)
    board.add_figure(wr)
    board.add_figure(wq)

    w_fig = board.white_figures

#    board.apply_net('white')
#    board.print_matrix()

#    print(board.tmp)
 
    for fig in w_fig:
        board.apply_figs()
        moves, captures = fig.possible_moves(board.matrix)
        totals = moves + captures
        previous = fig.position
        board.clear_matrix()
        for mov in totals:
            fig.move(mov)
            board.apply_net('white')
             #   print(board.tmp)
            if board.tmp[0][2] == Color.white.value:
                print(fig)
                print(fig.position)
                print("***************")
            board.clear_net()
            fig.move(previous)

#    def apply_figs(self):
#    def clear_matrix(self):
#    def clear_tmp(self):
#    def apply_net(self, color):

    #def move(self, new_pose):
    #def remove(self):
    #pos, cap = p.possible_moves(x)
    #print(pos)
    #print(cap)

#        if fig == wq:
#            print(moves)
#            print(captures)
#            print(totals)
#            print(board.matrix)
