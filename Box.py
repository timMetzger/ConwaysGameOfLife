import random

from p5 import square,fill

class Box:

    def __init__(self,x,y,size):
        self._x = x
        self._y = y
        self._size = size - 1
        self._alive = True if random.uniform(0,1) > 0.6 else False

    def display(self):
        if self._alive:
            fill(0)
        else:
            fill(255)
        square(self._x, self._y, self._size)

    def isalive(self):
        return self._alive

    def invigorate(self):
        self._alive = True

    def kill(self):
        self._alive = False

    def __str__(self):
        return f"(x,y):({self._x},{self._y}) --- Alive: {self._alive})"