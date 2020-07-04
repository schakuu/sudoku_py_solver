from puzzle.line import Line
from puzzle.panel import Panel


class Board:
    def __init__(self):
        self._panels = None
        self._rows = [Line(i) for i in range(0, 8)]
        self._cols = [Line(i) for i in range(0, 8)]
        for _row in range(0, 2):
            for _col in range(0, 2):
                self._panels[_row, _col] = Panel(_row, _col)

    def get_row(self, row_num):
        return self._rows[row_num]

    def get_col(self, col_num):
        return self._cols[col_num]
