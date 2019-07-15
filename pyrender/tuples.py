import functools
import numpy as np
import unittest

class Tuple(object):
    EPSILON = 0.00001 

    def __init__(self, x=0, y=0, z=0, w=0):
        self._tuple = np.array([x, y, z, w], dtype='float64')

    def __str__(self):
        return str(self._tuple)

    def __add__(self, other):
        res = self._tuple + other._tuple
        return self.__class__(res[0], res[1], res[2], res[3])

    def __sub__(self, other):
        res = self._tuple - other._tuple
        return self.__class__(res[0], res[1], res[2], res[3])

    def __mul__(self, scalar):
        res = self._tuple * scalar
        return self.__class__(res[0], res[1], res[2], res[3])

    def __truediv__(self, scalar):
        res = self._tuple / scalar
        return self.__class__(res[0], res[1], res[2], res[3])

    def __eq__(self, other):
        if np.all(np.abs(self._tuple - other._tuple) < self.EPSILON):
            return True
        return False

    def __neg__(self):
        res = -self._tuple
        return self.__class__(res[0], res[1], res[2], res[3])

    def Magnitude(self):
        return np.linalg.norm(self._tuple)

    def Normalize(self):
        res = self._tuple / self.Magnitude()
        return self.__class__(res[0], res[1], res[2], res[3])

    def IsPoint(self):
        if self._tuple[3] == 1:
            return True
        return False

    def IsVector(self):
        if self._tuple[3] == 0:
            return True
        return False

    @property
    def x(self):
        return self._tuple[0]

    @x.setter
    def x(self, value):
        self._tuple[0] = value

    @property
    def y(self):
        return self._tuple[1]

    @y.setter
    def y(self, value):
        self._tuple[1] = value

    @property
    def z(self):
        return self._tuple[2]

    @z.setter
    def z(self, value):
        self._tuple[2] = value

    @property
    def w(self):
        return self._tuple[3]

    @w.setter
    def w(self, value):
        self._tuple[3] = value

def Point(x, y, z):
    return Tuple(x, y, z, 1)

def Vector(x, y, z):
    return Tuple(x, y, z, 0)
