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


    check_fig = board.white_figures
    ref_fig = board.black_figures
    sol = []
    is_safe = False

    for fig in check_fig:                                                                               # for every white figure X
        is_safe = False
        board.apply_figs()
        moves, captures = fig.possible_moves(board.matrix)                                          # take its possible moves
        totals = moves + captures
        previous = fig.position
        for mov in totals:                                                                          # and for every move
            captured, fig_captured = board.move_figure(fig, mov) 
            board.apply_net('white')
            if board.tmp[black_king.position[0]][black_king.position[1]] != Color.white.value:      # if black king is not endangered => safe
                pass
            else:                                                                                   # if it is endangered
                for i in range(len(ref_fig)):
                    if is_safe == True:
                        is_safe = False
                        break
                    if ref_fig[i] != fig_captured:
                        board.apply_figs()
                        ref_moves, ref_captures = ref_fig[i].possible_moves(board.matrix)
                        ref_previous = ref_fig[i].position
                        ref_total = ref_moves + ref_captures
                        last = ref_fig[-1]
                        if ref_fig[i] == last and len(ref_total) == 0:
                            sol.append([fig, mov])
                        for j in range(len(ref_total)):
                            check_captured, check_fig_captured = board.move_figure(ref_fig[i], (ref_total[j]))                                
                            board.apply_net('white')
                            if board.tmp[black_king.position[0]][black_king.position[1]] != Color.white.value:      # if black king is not endangered => safe
                                ref_fig[i].move(ref_previous)        
                                is_safe = True
                                fig.move(previous)
                                break
                            else:
                                if ref_fig[i] == last and j == len(ref_total) - 1:
                                    sol.append([fig, mov])
                            if check_captured == True:
                                check_fig_captured.move(ref_total[j])
                            ref_fig[i].move(ref_previous)        
            if captured == True:
                fig_captured.move(mov)
            fig.move(previous)
    print(sol)

