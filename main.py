#!/usr/bin/env python3


import enum

class Color(enum.Enum):
    undefined = -1
    white = 0
    black = 1


class Knight:
    
    def __init__(self, pose, color):
        self.position = pose
        self.color = Color[color]

    def printing(self):
        print(self.color)

k = Knight([0, 0], 'black')
k.printing()

x = Color['undefined']
y = Color['black']
z = Color['white']


