import matplotlib.pyplot as plt
import numpy as np
import math

width = 100
height = 100

def check_input(side):
    try:
        return float(input(side))
    except ValueError:
        return None

def check_triangle(a, b, c):
    if math.isnan(a) or math.isnan(b) or math.isnan(c):
        return "Не треугольник"

    if (a <= 0 or b <= 0 or c <= 0):
        return "Не треугольник"

    elif a + b < c or a + c < b or b + c < a\
        or math.isclose(a + b, c) or math.isclose(a + c, b)\
        or math.isclose(b + c, a):
        return "Не треугольник"

    elif math.isclose(a, b) and math.isclose(a, c):
        return "Равносторонний"

    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        return "Равнобедренный"

    else:
        return "Разносторонний"

def vertices_coordinates(a: float, b: float, c: float) -> list[tuple[int, int]]:
    if a <= 0 or b <= 0 or c <= 0:
        return [(-1, -1)] * 3
    if a + b < c or a + c < b or b + c < a\
        or math.isclose(a + b, c) or math.isclose(a + c, b)\
        or math.isclose(b + c, a):
        return [(-1, -1)] * 3
    x1, y1 = 0, 0
    x2, y2 = c, 0

    cos_A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    sin_A = math.sqrt(1 - cos_A ** 2)

    x3 = b * cos_A
    y3 = b * sin_A

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

def draw_triangle(vertices):
    xs = []
    ys = []
    for x, y in vertices:
        xs.append(x)
        ys.append(y)
    xs.append(vertices[0][0])
    ys.append(vertices[0][1])

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(xs, ys, color='red', linewidth=2, label='Треугольник')

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')  # 1 единица X = 1 единица Y
    ax.grid(True, linestyle='-', alpha=0.7)
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    plt.show()