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
    b_fig = board.black_figures
    sol = []
    is_safe = False

    for fig in w_fig:                                                                               # for every white figure X
        is_safe = False
        board.apply_figs()
        moves, captures = fig.possible_moves(board.matrix)                                          # take its possible moves
        totals = moves + captures
        previous = fig.position
#        print("#" * 10)
#        print("Which figure now")
#        print(fig)
#        print(totals)
#        print("#" * 10)
        for mov in totals:                                                                          # and for every move
            fig.move(mov)                                                                           
            board.apply_net('white')
            if board.tmp[black_king.position[0]][black_king.position[1]] != Color.white.value:      # if black king is not endangered => safe
            #    print("King not endangered")
            #    print(fig)
            #    print(mov)
                pass
            else:                                                                                   # if it is endangered
                for i in range(len(b_fig)):
                    if is_safe == True:
                        is_safe = False
#                        print("OK")
                        break
                    board.apply_figs()
                    b_moves, b_captures = b_fig[i].possible_moves(board.matrix)
                    b_previous = b_fig[i].position
                    b_total = b_moves + b_captures
 #                   print(fig)
 #                   print(mov)
 #                   print(b_fig[i])
 #                   print(b_total)
                    last = b_fig[-1]
                    if b_fig[i] == last and len(b_total) == 0:
                        print("*" * 10)
                        print("Check mate!!!")
                        print(fig)
                        print(mov)
                        print("*" * 10)
                        sol.append([fig, mov])
                    for j in range(len(b_total)):
                        b_fig[i].move(b_total[j])
                        board.apply_net('white')
  #                      print("Konkretny ruch:")
  #                      print(b_fig[i])
  #                      print(b_total[j])
                        if board.tmp[black_king.position[0]][black_king.position[1]] != Color.white.value:      # if black king is not endangered => safe
   #                         print("King can be saved")
   #                         print(fig)
   #                         print(mov)
                            b_fig[i].move(b_previous)        
                            is_safe = True
                            fig.move(previous)
                            break
                        else:
                            if b_fig[i] == last and j == len(b_total) - 1:
                                print("*" * 10)
                                print("Check mate!!!")
                                print(fig)
                                print(mov)
                                print("*" * 10)
                                sol.append([fig, mov])
                        b_fig[i].move(b_previous)        
            fig.move(previous)



