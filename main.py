#!/usr/bin/env python3

from board import *

SIZE = 8

if __name__ == "__main__":
    
    board = Board(SIZE)

    for i in range(SIZE):
         line = input()
         elements = line.split()
         for j in range(len(elements)):
             el = elements[j]
             if el != '__':
                 if el[0] == 'w':
                     color = Color.white.name
                 else:
                     color = Color.black.name
                 if el[1] == 'p':
                     board.add_figure(Pawn([i, j], color))
                 elif el[1] == 'r':
                     board.add_figure(Rook([i, j], color))
                 elif el[1] == 'k':
                     board.add_figure(Knight([i, j], color))
                 elif el[1] == 'b':
                     board.add_figure(Bishop([i, j], color))
                 elif el[1] == 'q':
                     board.add_figure(Queen([i, j], color))
                 elif el[1] == 'W':
                     if color == 'white':
                        white_king = King([i, j], color)
                        board.add_figure(white_king)
                     else:
                         black_king = King([i, j], color)
                         board.add_figure(black_king)
    print(board.white_figures)
    print(board.black_figures)


#    bp = Pawn([5, 1], 'black')
#    wp = Pawn([6, 7], 'white')
#    bW = King([0, 2], 'black')
#    wW = King([7, 4], 'white')
#    wr = Rook([1, 4], 'white')
#    wq = Queen([3, 3], 'white')
#    board.add_figure(bp)
#    board.add_figure(wp)
#    board.add_figure(bW)
#    board.add_figure(wW)
#    board.add_figure(wr)
#    board.add_figure(wq)

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
            if board.tmp[black_king.position[0]][black_king.position[1]] == Color.white.value:
                king_moves, king_captures = black_king.possible_moves(board.matrix)
 #               if len(king_moves) == 0:
                                                            

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
