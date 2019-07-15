import functools
import numpy as np

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

    def __div__(self, scalar):
        res = self._tuple * scalar
        return self.__class__(res[0], res[1], res[2], res[3])

    def __eq__(self, other):
        if np.all(np.abs(self._tuple - other._tuple) < self.EPSILON):
            return True
        return False

    def __neg__(self):
        res = -self._tuple
        return self.__class__(res[0], res[1], res[2], res[3])

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

class Point(Tuple):
    def __init__(self, x=0, y=0, z=0, w=1):
        self._tuple = np.array([x, y, z, 1.0], dtype='float64')

    def _pointerize(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[-1], Point):
                res = func(*args, **kwargs)
                p = Point(res.x, res.y, res.z)
                return p
            else:
                return func(*args, **kwargs)
        return wrapper

    @_pointerize
    def __add__(self, other):
        return super().__add__(other)

    @_pointerize
    def __sub__(self, other):
        return super().__sub__(other)

    @property
    def w(self):
        return self._tuple[3]

    @w.setter
    def w(self, value):
        raise ValueError("w is Immutable for Points")

class Vector(Tuple):
    def __init__(self, x=0, y=0, z=0, w=0):
        self._tuple = np.array([x, y, z, 0.0], dtype='float64')

    def _vectorize(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[-1], Vector):
                res = func(*args, **kwargs)
                v = Vector(res.x, res.y, res.z)
                return v
            else:
                return func(*args, **kwargs)
        return wrapper

    @_vectorize
    def __add__(self, other):
        return super().__add__(other)

    @_vectorize
    def __sub__(self, other):
        return super().__sub__(other)

    @property
    def w(self):
        return self._tuple[3]

    @w.setter
    def w(self, value):
        raise ValueError("w is Immutable for Vectors")

v = Tuple(2,2,2,2)
print(v * 3.2)