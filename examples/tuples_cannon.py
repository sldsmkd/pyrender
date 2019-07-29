from pyrender.tuples import Point, Vector


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


p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normal)
e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

while p.position.y >= 0:
    print(p.position)
    p = tick(p, e)