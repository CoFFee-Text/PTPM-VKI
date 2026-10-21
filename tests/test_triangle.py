import unittest
from src.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_Calculate_Returns_Type_And_Coordinates(self):
        t = Triangle(3, 4, 5)
        triangle_type, coordinates = t.calculate()

        self.assertEqual(triangle_type, "Разносторонний")
        self.assertEqual(len(coordinates), 3, "Должно быть ровно 3 вершины")
        self.assertNotEqual(coordinates, [(-1, -1)] * 3, "Координаты не должны быть ошибочными")

    def test_calculate_handles_invalid_triangle(self):
        t = Triangle(1, 2, 10)
        triangle_type, coordinates = t.calculate()

        self.assertEqual(triangle_type, "Не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3, "При невалидных данных координаты сбрасываются")

if __name__ == "__main__":
    unittest.main()