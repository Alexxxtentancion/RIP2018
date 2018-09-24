from .geom_figure import Figure
import math


class Cirle_(Figure):
    def __init__(self, r, c):
        self.radius = r
        self.color = c

    def area(self):
        return math.pi * self.radius * self.radius


    def __repr__(self):
        return "radius = {},color = {},area = {}".format(
            self.radius,
            self.color,
            self.area()
        )