
class Game:
    def __init__(self, new_values=True, all_values=0):
        self.panels = [Panel(i, new_values, all_values) for i in range(0, 8)]
