from .rectangle import rectangle
from .figure_color import Color


class square(rectangle):
    def __init__(self, s, c):
        super(square, self).__init__(s,s,c)

    def area(self):
        return self.width * self.width

    def __repr__(self):
        return "Side = {},Color = {},Area = {}".format(
            self.width,
            self.color,
            self.area()
        )





