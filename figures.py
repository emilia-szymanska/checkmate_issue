#!/usr/bin/env python3

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

    def remove(self):
        self.position = [-1, -1]


class Rook:
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        size = len(board)
        captures = []
        free_moves = []
        v = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(v)):
            x = self.position[0]
            y = self.position[1]
            while True:
                if x + v[i][0] < size and  x + v[i][0] >= 0 and y + v[i][1] < size and y + v[i][1] >= 0:
                    content = board[x+v[i][0]][y+v[i][1]]
                    if content != self.color.value:
                        if content == 0:
                            x = x+v[i][0] 
                            y = y+v[i][1]
                            free_moves.append([x, y])
                        else:
                            captures.append([x+v[i][0], y+v[i][1]])
                            break
                    else:
                        break
                else:
                    break
        return free_moves, captures
    
    def move(self, new_pose):
        self.position = new_pose

    def remove(self):
        self.position = [-1, -1]


class Bishop:
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        size = len(board)
        captures = []
        free_moves = []
        v = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for i in range(len(v)):
            x = self.position[0]
            y = self.position[1]
            while True:
                if x + v[i][0] < size and  x + v[i][0] >= 0 and y + v[i][1] < size and y + v[i][1] >= 0:
                    content = board[x+v[i][0]][y+v[i][1]]
                    if content != self.color.value:
                        if content == 0:
                            x = x+v[i][0] 
                            y = y+v[i][1]
                            free_moves.append([x, y])
                        else:
                            captures.append([x+v[i][0], y+v[i][1]])
                            break
                    else:
                        break
                else:
                    break
        return free_moves, captures
    
    def move(self, new_pose):
        self.position = new_pose

    def remove(self):
        self.position = [-1, -1]


class Queen:
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        size = len(board)
        captures = []
        free_moves = []
        v = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(v)):
            x = self.position[0]
            y = self.position[1]
            while True:
                if x + v[i][0] < size and  x + v[i][0] >= 0 and y + v[i][1] < size and y + v[i][1] >= 0:
                    content = board[x+v[i][0]][y+v[i][1]]
                    if content != self.color.value:
                        if content == 0:
                            x = x+v[i][0] 
                            y = y+v[i][1]
                            free_moves.append([x, y])
                        else:
                            captures.append([x+v[i][0], y+v[i][1]])
                            break
                    else:
                        break
                else:
                    break
        return free_moves, captures
    
    def move(self, new_pose):
        self.position = new_pose

    def remove(self):
        self.position = [-1, -1]


class King:
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        size = len(board)
        captures = []
        free_moves = []
        v = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
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

    def remove(self):
        self.position = [-1, -1]


class Pawn:
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def possible_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        size = len(board)
        captures = []
        free_moves = []

        if self.color.name == 'white':                              # white figures are always on 1st and 2nd row
            if x - 1 >= 0:
                content = board[x-1][y]                             # white pawns always go to higher rows
                if content == 0:
                    free_moves.append([x-1, y])
                    if self.position[0] == size - 2:                # if a pawn hasn't moved yet, it can make a double move
                        content = board[x-2][y]
                        if content == 0:
                            free_moves.append([x-2, y])
                if y - 1 >= 0:                                      # captures differently than moves
                    content = board[x-1][y-1]
                    if content == Color.black.value:
                        captures.append([x-1, y-1])
                if y + 1 < size:
                    content = board[x-1][y+1]
                    if content == Color.black.value:
                        captures.append([x-1, y+1])
        else:                                                       # black figures are always on 7th and 8th row
            if x + 1 < size:
                content = board[x+1][y]
                if content == 0:                                    # black pawns always go to lower rows
                    free_moves.append([x+1, y])
                    if self.position[0] == 1:                       # if a pawn hasn't moved yet, it can make a double move
                        content = board[x+2][y]
                        if content == 0:
                            free_moves.append([x+2, y])
                if y - 1 >= 0:
                    content = board[x+1][y-1]
                    if content == Color.white.value:
                        captures.append([x+1, y-1])
                if y + 1 < size:
                    content = board[x+1][y+1]
                    if content == Color.white.value:
                        captures.append([x+1, y+1])
        
        return free_moves, captures
    
    def move(self, new_pose):
        self.position = new_pose

    def remove(self):
        self.position = [-1, -1]
