import unittest
from math import nan
from math import inf
from src.triangle import check_triangle, vertices_coordinates


class TestTriangle(unittest.TestCase):

    # check_triangle
    def test_Nan_Sides(self):
        self.assertEqual(check_triangle(nan, nan, nan), "Не треугольник", "nan в любой позиции 'Не треугольник'")

    def test_Equilateral_Triangle(self):
        self.assertEqual(check_triangle(10, 10, 10), "Равносторонний")

    def test_Isosceles_Triangle(self):
        self.assertEqual(check_triangle(10, 6, 6), "Равнобедренный")

    def test_Scalene_Triangle(self):
        self.assertEqual(check_triangle(3, 4, 5), "Разносторонний")

    def test_Negative_Sides(self):
        self.assertEqual(check_triangle(-10000, -10000, -10000), "Не треугольник", "Отрицательные стороны не должны образовывать треугольник")

    def test_One_Zero_Side(self):
        self.assertEqual(check_triangle(0, 10, 10), "Не треугольник", "Стороны равные 0 не должны образовывать треугольник")

    def test_Zero_Sides(self):
        self.assertEqual(check_triangle(0, 0, 0), "Не треугольник", "Стороны равные 0 не должны образовывать треугольник")

    def test_Float_Sides_NotTriangle(self):
        self.assertEqual(check_triangle(1.0, 2.0, 3.0000000000000004), "Не треугольник", "Сумма двух сторон должна быть строго больше третьей")

    def test_Float_Sides_Triangle(self):
        self.assertEqual(check_triangle(3.5, 4.5, 5.5), "Разносторонний")

    def test_Borderline_Case_NotTriangle(self):
        self.assertEqual(check_triangle(1, 2, 3), "Не треугольник", "Сумма двух сторон должна быть строго больше третьей")

    def test_Very_Small_Sides_Triangle(self):
        self.assertEqual(check_triangle(1e-10, 1e-10, 1e-10), "Равносторонний")

    def test_One_Inf_Side(self):
        self.assertEqual(check_triangle(inf, 10, 10), "Не треугольник")

    def test_Inf_Sides(self):
        self.assertEqual(check_triangle(inf, inf, inf), "Не треугольник")

    # vertices_coordinates
    def test_Nan_Coordinates(self):
        self.assertEqual(vertices_coordinates(nan, nan, nan), [(-1,-1)]*3)

    def test_Very_Small_Coordinates(self):
        result = vertices_coordinates(1e-10, 1e-10, 1e-10)
        self.assertNotEqual(result, [(-1, -1)] * 3,"Треугольник с очень маленькими сторонами существует и входит в поле")
        self.assertNotEqual(result, [(-2, -2)] * 3,"1e-10 -- число, не нечисловые данные")

    def test_Vertices_Equilateral(self):
        self.assertNotEqual(vertices_coordinates(5, 5, 5), [(-1,-1)]*3)

    def test_Vertices_Rectangular(self):
        self.assertNotEqual(vertices_coordinates(3, 4, 5), [(-1,-1)]*3)

    def test_Vertices_Sharpangled(self):
        self.assertNotEqual(vertices_coordinates(6, 7, 8), [(-1,-1)]*3)

    def test_Very_Big_Coordinates(self):
        result = vertices_coordinates(1e-10, 1e-10, 1e-10)
        self.assertNotEqual(result, [(-1,-1)]*3, "Треугольник с очень большими сторонами существует и входит в поле")
        self.assertNotEqual(result, [(-2, -2)] * 3,"1e10 -- число, не нечисловые данные")

    def test_Vertices_Bluntangled(self):
        self.assertNotEqual(vertices_coordinates(6, 6, 10), [(-1,-1)]*3)

    def test_Vertices_Bluntangled2(self):
        self.assertNotEqual(vertices_coordinates(10, 6, 6), [(-1,-1)]*3) # вот этот с подвохом

if __name__ == "__main__":
    unittest.main()