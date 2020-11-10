#!/usr/bin/env python3

from board import *

def checkmate(board, color):
    if color == 'white':    
        check_fig = board.white_figures
        ref_fig = board.black_figures
        check_col = Color.white
        ref_col = Color.black
        ref_king = board.black_king 
    else:
        check_fig = board.black_figures
        ref_fig = board.white_figures
        check_col = Color.black
        ref_col = Color.white
        ref_king = board.white_king 
    
    king_x = ref_king.position[0]
    king_y = ref_king.position[1]

    solution = []
    is_safe = False
    
    for fig in check_fig:                                                                                           # for every figure of color X
        is_safe = False
        board.apply_figs()
        moves, captures = fig.possible_moves(board.matrix) 
        all_moves = moves + captures
        previous = fig.position
        for mov in all_moves:                                                                                       # simulate every possible movement 
            captured, fig_captured = board.move_figure(fig, mov) 
            board.apply_net(check_col.name)
            if board.tmp[king_x][king_y] == check_col.value:                                                        # is king of color Y on endangered spot?
                for i in range(len(ref_fig)):                                                                       # if yes, then take every figure Y
                    if is_safe:                                                                                     # simulate its move
                        is_safe = False
                        break
                    if ref_fig[i] != fig_captured:
                        board.apply_figs()
                        ref_moves, ref_captures = ref_fig[i].possible_moves(board.matrix)
                        ref_previous = ref_fig[i].position
                        ref_total = ref_moves + ref_captures
                        last = ref_fig[-1]
                        if ref_fig[i] == last and len(ref_total) == 0:                                              
                            solution.append([fig, mov])
                        for j in range(len(ref_total)):
                            check_captured, check_fig_captured = board.move_figure(ref_fig[i], (ref_total[j]))                                
                            board.apply_net(check_col.name)
                            king_xx = ref_king.position[0]
                            king_yy = ref_king.position[1]
                            if board.tmp[king_xx][king_yy] != check_col.value:                                      # if a Y figure which saves the king exists
                                ref_fig[i].move(ref_previous)                                                       # analyse next movements of figure X
                                is_safe = True
                                fig.move(previous)
                                break
                            else:
                                if ref_fig[i] == last and j == len(ref_total) - 1:                                  # if such a figure doesn't exist
                                    solution.append([fig, mov])                                                     # CHECK MATE
                            if check_captured == True:
                                check_fig_captured.move(ref_total[j])
                            ref_fig[i].move(ref_previous)        
            if captured == True:
                fig_captured.move(mov)
            fig.move(previous)
    return solution
