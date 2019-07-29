# -- FILE: features/steps/canvas_steps.py
from behave import given, when, then
from pyrender.tuples import Color
from pyrender.canvas import Canvas


@given(u'c ← Canvas(10, 20)')
def step_impl(context):
    context.c = Canvas(10, 20)


@then(u'c.width = 10')
def step_impl(context):
    assert context.c.width == 10


@then(u'c.height = 20')
def step_impl(context):
    assert context.c.height == 20


@then(u'every pixel of c is Color(0, 0, 0)')
def step_impl(context):
    for x in range(context.c.width):
        for y in range(context.c.height):
            assert context.c.get_pixel(x, y) == Color(0, 0, 0)


@given(u'red ← Color(1, 0, 0)')
def step_impl(context):
    context.red = Color(1, 0, 0)


@when(u'c.set_pixel(2, 3, red)')
def step_impl(context):
    context.c.set_pixel(2, 3, context.red)


@then(u'c.get_pixel(c, 2, 3) = red')
def step_impl(context):
    assert context.c.get_pixel(2, 3) == context.red


@given(u'c ← Canvas(5, 3)')
def step_impl(context):
    context.c = Canvas(5, 3)


@when(u'ppm ← c.ppm')
def step_impl(context):
    context.ppm = context.c.ppm.splitlines(True)


@then(u'lines 1-3 of ppm are')
def step_impl(context):
    assert context.ppm[0] == "P3\n"
    assert context.ppm[1] == "5 3\n"
    assert context.ppm[2] == "255\n"


@given(u'c1 ← Color(1.5, 0, 0)')
def step_impl(context):
    context.c1 = Color(1.5, 0, 0)


@given(u'c2 ← Color(0, 0.5, 0)')
def step_impl(context):
    context.c2 = Color(0, 0.5, 0)


@given(u'c3 ← Color(-0.5, 0, 1)')
def step_impl(context):
    context.c3 = Color(-0.5, 0, 1)


@when(u'c.set_pixel(0, 0, c1)')
def step_impl(context):
    context.c.set_pixel(0, 0, context.c1)


@when(u'c.set_pixel(2, 1, c2)')
def step_impl(context):
    context.c.set_pixel(2, 1, context.c2)


@when(u'c.set_pixel(4, 2, c3)')
def step_impl(context):
    context.c.set_pixel(4, 2, context.c3)


@then(u'lines 4-6 of ppm are')
def step_impl(context):
    print(context.ppm)
    assert context.ppm[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
    assert context.ppm[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n"
    assert context.ppm[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"

@given(u'c ← Canvas(10, 2)')
def step_impl(context):
    context.c = Canvas(10, 2)


@when(u'every pixel of c is set to Color(1, 0.8, 0.6)')
def step_impl(context):
    for x in range(context.c.width):
        for y in range(context.c.height):
            context.c.set_pixel(x, y, Color(1, 0.8, 0.6))


@then(u'lines 4-7 of ppm are')
def step_impl(context):
    assert context.ppm[3] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n"
    assert context.ppm[4] == "153 255 204 153 255 204 153 255 204 153 255 204 153\n"
    assert context.ppm[5] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n"
    assert context.ppm[6] == "153 255 204 153 255 204 153 255 204 153 255 204 153\n"

@then(u'ppm ends with a newline character')
def step_impl(context):
    assert context.ppm[6] == "\n"
