from puzzle.square import Square
from puzzle.grouping import Group

"""
Represents a set of nine elements in a 3x3 square.  
"""


class Panel(Group):
    def __init__(self):
        self.values = [[Square(0, 0, 0, 0) for i in range(0, 3)] for j in range(0, 3)]

    def set_values(self, values, delimiter=' '):
        for i, u in enumerate(values.split(",")):
            for j, v in enumerate(u.split()):
                self.values[i][j].set_value(int(v))

    def child_values(self):
        child_v = []
        for i in range(0, 3):
            child_v += [_s.get_value() for _s in self.values[i]]
        return child_v
