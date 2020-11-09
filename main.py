#!/usr/bin/env python3

x = [
    [0, 0, 0, 0, 1],
    [0, 0, 2, 0, 0], 
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

import enum

class Color(enum.Enum):
    undefined = -1
    white = 0
    black = 1


class Knight:
    
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        size = len(board)
        v = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        possible_pos = []
        
        for i in range(len(v)):
            if x + v[i][0] < size and  x + v[i][0] >= 0 and y + v[i][1] < size and y + v[i][1] >= 0:
                if board[x+v[i][0]][y+v[i][1]] == 0:
                    possible_pos.append([x+v[i][0], y+v[i][1]])
        
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
        print(board[4])
        return possible_pos
    


k = Knight([1, 2], 'black')
pos = k.possible_moves(x)
print(pos)

x = Color['undefined']
y = Color['black']
z = Color['white']


