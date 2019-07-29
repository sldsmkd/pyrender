from pyrender.tuples import Color, Point, Vector
from pyrender.canvas import Canvas


class Projectile:
    position: Point
    velocity: Vector

    def __init__(self, position: Point, velocity: Vector):
        self.position = position
        self.velocity = velocity


class Environment:
    gravity: Vector
    wind: Vector

    def __init__(self, gravity: Vector, wind: Vector):
        self.gravity = gravity
        self.wind = wind


def tick(proj: Projectile, env: Environment):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


start = Point(0, 1, 0)
velocity = Vector(1, 1.8, 0).normal * 11.25
p = Projectile(start, velocity)

gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)

e = Environment(gravity, wind)

c = Canvas(900, 550)
color = Color(1.0, 0, 0)

while p.position.y >= 0:
    c.set_pixel(int(p.position.x), 500 - int(p.position.y), color)
    p = tick(p, e)

print(c.ppm)
