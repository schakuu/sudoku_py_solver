
"""
    Square is the lowest element of the board
    The reason this is its own class is because both a Panel and a Line need a reference to this object

    A Square has a single integer value. The default value is zero, which is also the same as the square being empty
    A square value can range between 1 and 9. Any other value renders the square invalid
"""


class Square:
    def __init__(self, panel_row, panel_col, board_row, board_col, value=0):
        self._panel_row = panel_row
        self._panel_col = panel_col
        self._board_row = board_row
        self._board_col = board_col
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def is_valid(self):
        return self._value in range(0, 9)