from math import sqrt


class point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        pass

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy
        pass

    def move_to(self, x, y):
        self._x = x
        self._y = y
        pass

    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx**2 + dy**2)
        pass

    def show(self):
        print('%2d::%2d' % (self._x, self._y))
        pass

    pass


def main():
    p = point(35, 40)
    p.move_by(10, 20)
    p.show()
    p.move_to(30, 30)
    p.show()
    po = point(60, 60)
    d = p.distance(po)
    print(d)
    pass


if __name__ == "__main__":
    main()
    pass