class Color:
    def __init__(self, c):
        self._color = c

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
