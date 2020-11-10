#!/usr/bin/env python3

from checkmate_algorithm import *

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
                        board.white_king = white_king
                     else:
                        black_king = King([i, j], color)
                        board.add_figure(black_king)
                        board.black_king = black_king
    
    
    solution = checkmate(board, 'white')
    win_color = 'white'
    if len(solution) == 0:
        solution = checkmate(board, 'black')
        win_color = 'black'
    
    for sol in solution:
        letter_begin = chr(ord('A') + sol[0].position[1]) 
        letter_end = chr(ord('A') + sol[1][1]) 
        print("Move your " + win_color + " figure from " + letter_begin + str(SIZE - sol[0].position[0]) + " to " + letter_end + str(SIZE - sol[1][0]))

