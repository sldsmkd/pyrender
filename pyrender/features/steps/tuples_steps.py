# -- FILE: features/steps/tuples_steps.py
from behave import given, when, then
from math import sqrt
from pyrender.tuples import Color, Point, Tuple, Vector
from pyrender.tuples import cross, dot, is_point, is_vector


@given(u'a ← Tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = Tuple(4.3, -4.2, 3.1, 1.0)


@then(u'a.x = 4.3')
def step_impl(context):
    assert context.a.x == 4.3


@then(u'a.y = -4.2')
def step_impl(context):
    assert context.a.y == -4.2


@then(u'a.z = 3.1')
def step_impl(context):
    assert context.a.z == 3.1


@then(u'a.w = 1.0')
def step_impl(context):
    assert context.a.w == 1.0


@then(u'a is a point')
def step_impl(context):
    assert is_point(context.a) is True


@then(u'a is not a vector')
def step_impl(context):
    assert is_vector(context.a) is False


@given(u'a ← Tuple(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.a = Tuple(4.3, -4.2, 3.1, 0.0)


@then(u'a.w = 0.0')
def step_impl(context):
    assert context.a.w == 0.0


@then(u'a is not a point')
def step_impl(context):
    assert is_point(context.a) is False


@then(u'a is a vector')
def step_impl(context):
    assert is_vector(context.a) is True


@given(u'p ← Point(4, -4, 3)')
def step_impl(context):
    context.p = Point(4, -4, 3)


@then(u'p = Tuple(4, -4, 3, 1)')
def step_impl(context):
    assert context.p == Tuple(4, -4, 3, 1)


@given(u'v ← Vector(4, -4, 3)')
def step_impl(context):
    context.v = Vector(4, -4, 3)


@then(u'v = Tuple(4, -4, 3, 0)')
def step_impl(context):
    assert context.v == Tuple(4, -4, 3, 0)


@given(u'a1 ← Tuple(3, -2, 5, 1)')
def step_impl(context):
    context.a1 = Tuple(3, -2, 5, 1)


@given(u'a2 ← Tuple(-2, 3, 1, 0)')
def step_impl(context):
    context.a2 = Tuple(-2, 3, 1, 0)


@then(u'a1 + a2 = Tuple(1, 1, 6, 1)')
def step_impl(context):
    assert context.a1 + context.a2 == Tuple(1, 1, 6, 1)


@given(u'p1 ← Point(3, 2, 1)')
def step_impl(context):
    context.p1 = Point(3, 2, 1)


@given(u'p2 ← Point(5, 6, 7)')
def step_impl(context):
    context.p2 = Point(5, 6, 7)


@then(u'p1 - p2 = Vector(-2, -4, -6)')
def step_impl(context):
    assert context.p1 - context.p2 == Vector(-2, -4, -6)


@given(u'p ← Point(3, 2, 1)')
def step_impl(context):
    context.p = Point(3, 2, 1)


@given(u'v ← Vector(5, 6, 7)')
def step_impl(context):
    context.v = Vector(5, 6, 7)


@then(u'p - v = Point(-2, -4, -6)')
def step_impl(context):
    assert context.p - context.v == Point(-2, -4, -6)


@given(u'v1 ← Vector(3, 2, 1)')
def step_impl(context):
    context.v1 = Vector(3, 2, 1)


@given(u'v2 ← Vector(5, 6, 7)')
def step_impl(context):
    context.v2 = Vector(5, 6, 7)


@then(u'v1 - v2 = Vector(-2, -4, -6)')
def step_impl(context):
    assert context.v1 - context.v2 == Vector(-2, -4, -6)


@given(u'zero ← Vector(0, 0, 0)')
def step_impl(context):
    context.zero = Vector(0, 0, 0)


@given(u'v ← Vector(1, -2, 3)')
def step_impl(context):
    context.v = Vector(1, -2, 3)


@then(u'zero - v = Vector(-1, 2, -3)')
def step_impl(context):
    assert context.zero - context.v == Vector(-1, 2, -3)


@given(u'a ← Tuple(1, -2, 3, -4)')
def step_impl(context):
    context.a = Tuple(1, -2, 3, -4)


@then(u'-a = Tuple(-1, 2, -3, 4)')
def step_impl(context):
    assert -context.a == Tuple(-1, 2, -3, 4)


@then(u'a * 3.5 = Tuple(3.5, -7, 10.5, -14)')
def step_impl(context):
    assert context.a * 3.5 == Tuple(3.5, -7, 10.5, -14)


@then(u'a * 0.5 = Tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert context.a * 0.5 == Tuple(0.5, -1, 1.5, -2)


@then(u'a / 2 = Tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert context.a / 2 == Tuple(0.5, -1, 1.5, -2)


@given(u'v ← Vector(1, 0, 0)')
def step_impl(context):
    context.v = Vector(1, 0, 0)


@then(u'magnitude(v) = 1')
def step_impl(context):
    assert context.v.magnitude == 1


@given(u'v ← Vector(0, 1, 0)')
def step_impl(context):
    context.v = Vector(0, 1, 0)


@given(u'v ← Vector(0, 0, 1)')
def step_impl(context):
    context.v = Vector(0, 0, 1)


@given(u'v ← Vector(1, 2, 3)')
def step_impl(context):
    context.v = Vector(1, 2, 3)


@then(u'magnitude(v) = √14')
def step_impl(context):
    assert context.v.magnitude == sqrt(14)

@given(u'v ← Vector(-1, -2, -3)')
def step_impl(context):
    context.v = Vector(-1, -2, -3)

@given(u'v ← Vector(4, 0, 0)')
def step_impl(context):
    context.v = Vector(4, 0, 0)

@then(u'normalize(v) = Vector(1, 0, 0)')
def step_impl(context):
    print(context.v.normal)
    assert context.v.normal == Vector(1, 0, 0)

@then(u'normalize(v) = approximately Vector(0.26726, 0.53452, 0.80178)')
def step_impl(context):
    assert context.v.normal == Vector(0.26726, 0.53452, 0.80178)

@when(u'norm ← normalize(v)')
def step_impl(context):
    context.norm = context.v.normal

@then(u'magnitude(norm) = 1')
def step_impl(context):
    assert context.norm.magnitude == 1

@given(u'a ← Vector(1, 2, 3)')
def step_impl(context):
    context.a = Vector(1, 2, 3)

@given(u'b ← Vector(2, 3, 4)')
def step_impl(context):
    context.b = Vector(2, 3, 4)

@then(u'dot(a, b) = 20')
def step_impl(context):
    assert dot(context.a, context.b) == 20

@then(u'cross(a, b) = Vector(-1, 2, -1)')
def step_impl(context):
    assert cross(context.a, context.b) == Vector(-1, 2, -1)

@then(u'cross(b, a) = Vector(1, -2, 1)')
def step_impl(context):
    assert cross(context.b, context.a) == Vector(1, -2, 1)

@given(u'c ← Color(-0.5, 0.4, 1.7)')
def step_impl(context):
    context.c = Color(-0.5, 0.4, 1.7)

@then(u'c.red = -0.5')
def step_impl(context):
    assert context.c.red == -0.5

@then(u'c.green = 0.4')
def step_impl(context):
    assert context.c.green == 0.4

@then(u'c.blue = 1.7')
def step_impl(context):
    assert context.c.blue == 1.7

@given(u'c1 ← Color(0.9, 0.6, 0.75)')
def step_impl(context):
    context.c1 = Color(0.9, 0.6, 0.75)

@given(u'c2 ← Color(0.7, 0.1, 0.25)')
def step_impl(context):
    context.c2 = Color(0.7, 0.1, 0.25)

@then(u'c1 + c2 = Color(1.6, 0.7, 1.0)')
def step_impl(context):
    assert context.c1 + context.c2 == Color(1.6, 0.7, 1.0)

@then(u'c1 - c2 = Color(0.2, 0.5, 0.5)')
def step_impl(context):
    assert context.c1 - context.c2 == Color(0.2, 0.5, 0.5)

@given(u'c ← Color(0.2, 0.3, 0.4)')
def step_impl(context):
    context.c = Color(0.2, 0.3, 0.4)

@then(u'c * 2 = Color(0.4, 0.6, 0.8)')
def step_impl(context):
    assert context.c * 2 == Color(0.4, 0.6, 0.8)

@given(u'c1 ← Color(1, 0.2, 0.4)')
def step_impl(context):
    context.c1 = Color(1, 0.2, 0.4)

@given(u'c2 ← Color(0.9, 1, 0.1)')
def step_impl(context):
    context.c2 = Color(0.9, 1, 0.1)

@then(u'c1 * c2 = Color(0.9, 0.2, 0.04)')
def step_impl(context):
    assert context.c1 * context.c2 == Color(0.9, 0.2, 0.04)

@given(u'v ← Vector(1, -1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given v ← Vector(1, -1, 0)')


@given(u'n ← Vector(0, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given n ← Vector(0, 1, 0)')


@when(u'r ← reflect(v, n)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When r ← reflect(v, n)')


@then(u'r = Vector(1, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = Vector(1, 1, 0)')


@given(u'v ← Vector(0, -1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given v ← Vector(0, -1, 0)')


@given(u'n ← Vector(√2/2, √2/2, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given n ← Vector(√2/2, √2/2, 0)')


@then(u'r = Vector(1, 0, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then r = Vector(1, 0, 0)')