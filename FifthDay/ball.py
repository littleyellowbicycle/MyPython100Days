from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self._alive = True

    def move(self, screen):
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 or self._x + self._radius > screen.get_width(
        ):
            self._sx = -self._sx
        if self._y - self._radius <= 0 or self._y + self._radius > screen.get_height(
        ):
            self._sy = -self._sy
        pass

    def eat(self, other):
        if self._alive and other._alive and self != other:
            distance = sqrt((self._x - other._x)**2 + (self._y - other._y)**2)
            if distance < self._radius + other._radius \
                    and self._radius > other._radius:
                other._alive = False
                self._radius = self._radius + int(other._radius * 0.146)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y),
                           self._radius, 0)
        pass

    pass