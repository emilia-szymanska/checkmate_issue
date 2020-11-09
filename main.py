#!/usr/bin/env python3

x = [
    [0, 0, 0, 0, 1],
    [0, 0, 2, 0, 0], 
    [0, 2, 1, 0, 2],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

import enum

class Color(enum.Enum):
    undefined = -1
    white = 1
    black = 2


class Knight:
    
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        size = len(board)
        v = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        captures = []
        free_moves = []
        
        for i in range(len(v)):
            if x + v[i][0] < size and  x + v[i][0] >= 0 and y + v[i][1] < size and y + v[i][1] >= 0:
                content = board[x+v[i][0]][y+v[i][1]]
                if content != self.color.value:
                    if content == 0:
                        free_moves.append([x+v[i][0], y+v[i][1]])
                    else:
                        captures.append([x+v[i][0], y+v[i][1]])

        return free_moves, captures

    
    def move(self, new_pose):
        self.position = new_pose


class Rook:
    
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        size = len(board)
        captures = []
        free_moves = []
        
        if y != size-1:
            i = 1
            while y + i < size:
                content = board[x][y+i]
                if content != self.color.value:
                    if content == 0:
                        free_moves.append([x, y+i])
                    else:
                        captures.append([x, y+i])
                        break
                else:
                    break
                i += 1
        
        if y != 0:
            i = 1
            while y - i >= 0:
                content = board[x][y-i]
                if content != self.color.value:
                    if content == 0:
                        free_moves.append([x, y-i])
                    else:
                        captures.append([x, y-i])
                        break
                else:
                    break
                i += 1
        
        if x != 0:
            i = 1
            while x - i >= 0:
                content = board[x-i][y]
                if content != self.color.value:
                    if content == 0:
                        free_moves.append([x-i, y])
                    else:
                        captures.append([x-i, y])
                        break
                else:
                    break
                i += 1

        if x != size-1:
            i = 1
            while x + i < size:
                content = board[x+i][y]
                if content != self.color.value:
                    if content == 0:
                        free_moves.append([x+i, y])
                    else:
                        captures.append([x+i, y])
                        break
                else:
                    break
                i += 1
        return free_moves, captures

    
    def move(self, new_pose):
        self.position = new_pose




k = Knight([1, 2], 'black')
r = Rook([2, 2], 'black')
pos, cap = r.possible_moves(x)
print(pos)
print(cap)

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
