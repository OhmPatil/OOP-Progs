import math


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eucliddist(self, new):
        x1 = self.x
        x2 = new.x
        y1 = self.y
        y2 = new.y

        distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        return distance


p1 = Points(1, 1)

p2 = Points(2, 2)

print(round(p2.eucliddist(p1), 2))
