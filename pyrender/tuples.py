import numpy as np


class PyrenderTuple():
    def __init__(self, x=0, y=0, z=0, w=0):
        self._data = np.array([x, y, z, w], dtype='float64')

    def _construct(self, res):
        return self.__class__(res[0], res[1], res[2], res[3])

    @property
    def magnitude(self):
        return sum(self._data * self._data) ** 0.5

    @property
    def normal(self):
        return self._construct(self._data / np.sqrt((self._data ** 2).sum()))

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return self._data

    def __eq__(self, other):
        EPSILON = 0.00001
        if np.all(np.abs(self._data - other.__repr__()) < EPSILON):
            return True
        return False

    def __add__(self, other):
        return self._construct(self._data + other.__repr__())

    def __sub__(self, other):
        return self._construct(self._data - other.__repr__())

    def __mul__(self, multiplyer):
        try:
            return self._construct(self._data * multiplyer)
        except TypeError:
            return self._construct(self._data * multiplyer.__repr__())

    def __truediv__(self, divisor):
        try:
            return self._construct(self._data / divisor)
        except TypeError:
            return self._construct(self._data / divisor.__repr__())

    def __neg__(self):
        return self._construct(-self._data)


class Color(PyrenderTuple):
    def __init__(self, red=0, green=0, blue=0):
        self._data = np.array([red, green, blue, 0], dtype='float64')

    def _construct(self, res):
        return self.__class__(res[0], res[1], res[2])

    @property
    def red(self):
        return self._data[0]

    @property
    def green(self):
        return self._data[1]

    @property
    def blue(self):
        return self._data[2]


class Tuple(PyrenderTuple):
    def __init__(self, x=0, y=0, z=0, w=0):
        self._data = np.array([x, y, z, w], dtype='float64')

    @property
    def x(self):
        return self._data[0]

    @property
    def y(self):
        return self._data[1]

    @property
    def z(self):
        return self._data[2]

    @property
    def w(self):
        return self._data[3]


class Point(Tuple):
    def __init__(self, x=0, y=0, z=0):
        self._data = np.array([x, y, z, 1], dtype='float64')

    def _construct(self, res):
        if res[3] == 0:
            return Vector(res[0], res[1], res[2])
        elif res[3] == 1:
            return Point(res[0], res[1], res[2])
        else:
            return Tuple(res[0], res[1], res[2], res[3])


class Vector(Tuple):
    def __init__(self, x=0, y=0, z=0):
        self._data = np.array([x, y, z, 0], dtype='float64')

    def _construct(self, res):
        if res[3] == 0:
            return Vector(res[0], res[1], res[2])
        elif res[3] == 1:
            return Point(res[0], res[1], res[2])
        else:
            return Tuple(res[0], res[1], res[2], res[3])


def cross(a, b):
    res = np.append(np.cross(a.__repr__()[0:3], b.__repr__()[0:3]), [0])
    return Vector(res[0], res[1], res[2])


def dot(a, b):
    return np.dot(a.__repr__(), b.__repr__())


def is_point(a):
    if a.w == 1.0:
        return True
    return False


def is_vector(a):
    if a.w == 0.0:
        return True
    return False
