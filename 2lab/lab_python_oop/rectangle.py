from .geom_figure import Figure
from .figure_color import Color


class rectangle(Figure):
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.color = Color(c).color

    def area(self):
        return self.width * self.height

    def _repr(self):
        return "width = {},height = {},color = {},area = {}".format(
            self.width,
            self.height,
            self.color,
            self.area()
        )