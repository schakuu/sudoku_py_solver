from puzzle.square import Square
from puzzle.grouping import Group

"""
Represents a set of nine elements in either a row or a column.  
"""


class Line(Group):
    def __init__(self):
        self._values = [Square(0, 0, 0, 0) for i in range(0, 9)]

    def set_values(self, values, delimiter=' '):
        for n, v in enumerate(values.split()):
            self._values[n].set_value(int(v))

    def child_values(self):
        return [_s.get_value() for _s in self._values]
