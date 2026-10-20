import math

width = 100
height = 100

class Triangle:
    def __init__(self, a, b, c):
        self.a = a  # атрибут экземпляра
        self.b = b  # атрибут экземпляра
        self.c = c

    def check_triangle(self):
        if (math.isnan(self.a) or math.isnan(self.b) or math.isnan(self.c)):
            return "Не треугольник"

        if (self.a <= 0 or self.b <= 0 or self.c <= 0):
            return "Не треугольник"

        elif (self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a \
                or math.isclose(self.a + self.b, self.c) or math.isclose(self.a + self.c, self.b) \
                or math.isclose(self.b + self.c, self.a)):
            return "Не треугольник"

        elif (math.isclose(self.a, self.b) and math.isclose(self.a, self.c)):
            return "Равносторонний"

        elif (math.isclose(self.a, self.b) or math.isclose(self.b, self.c) or math.isclose(self.a, self.c)):
            return "Равнобедренный"

        else:
            return "Разносторонний"

    def vertices_coordinates(self) -> list[tuple[int, int]]:
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return [(-1, -1)] * 3
        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a \
                or math.isclose(self.a + self.b, self.c) or math.isclose(self.a + self.c, self.b) \
                or math.isclose(self.b + self.c, self.a):
            return [(-1, -1)] * 3
        x1, y1 = 0, 0
        x2, y2 = self.c, 0

        cos_A = (self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)
        sin_A = math.sqrt(1 - cos_A ** 2)

        x3 = self.b * cos_A
        y3 = self.b * sin_A

        coordinates = [(x1, y1), (x2, y2), (x3, y3)]

        max_x = max(p[0] for p in coordinates)
        max_y = max(p[1] for p in coordinates)

        if max_x <= 0 or max_y <= 0:
            return [(-1, -1)] * 3
        scale = min(width / max_x, height / max_y)

        result = []
        for x, y in coordinates:
            result.append((round(x * scale), round(y * scale)))
        return result

    def calculate(self) -> tuple[str, list[tuple[int, int]]]:
        triangle_type = self.check_triangle()
        coordinates = self.vertices_coordinates()
        return triangle_type, coordinates