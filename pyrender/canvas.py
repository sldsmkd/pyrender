from pyrender.tuples import Color
from textwrap import wrap

class Canvas():
    def __init__(self, width: int, height: int):
        self._canvas = [[Color() for j in range(width)] for i in range(height)]

    @property
    def height(self):
        return len(self._canvas)

    @property
    def width(self):
        return len(self._canvas[-1])

    def get_pixel(self, x: int, y: int):
        return self._canvas[y][x]

    def set_pixel(self, x: int, y: int, color: Color):
        self._canvas[y][x] = color

    @property
    def ppm(self):

        def create_header():
            header = "P3\n"
            header += str(self.width) + " " + str(self.height) + "\n"
            header += "255\n"
            return header

        def create_body():
            body = ""

            def clamp(val):
                return str(max(0, min(int(round(val * 255)), 255)))

            for y in range(self.height):
                row = ""
                for x in range(self.width):
                    pixel = self.get_pixel(x, y)
                    row += clamp(pixel.red) + " "
                    row += clamp(pixel.green) + " "
                    row += clamp(pixel.blue) + " "
                rows = wrap(row)
                for row in rows:
                    body += row + ("\n")
            return body + "\n"

        ppm = ""
        ppm += create_header()
        ppm += create_body()
        return ppm
