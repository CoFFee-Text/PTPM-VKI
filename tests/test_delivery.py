import unittest
from src.Delivery import *

class TestDelivery(unittest.TestCase):
    def test_ValidData(self):
        self.assertEqual(calculate_delivery_cost(20, 150, "обычный"), (1425, "2026-09-04"))

    def test_Too_Small_Weight(self):
        self.assertEqual(calculate_delivery_cost(-0.1, 150, "обычный"), (-1, "0000-00-00"), "Вес не может быть меньше 0 кг")

    def test_Too_Large_Weight(self):
        self.assertEqual(calculate_delivery_cost(50.1, 150, "обычный"), (-1, "0000-00-00"), "Вес не может быть больше 50.0 кг")

    def test_Too_Small_Distance(self):
        self.assertEqual(calculate_delivery_cost(10, 0, "обычный"), (-1, "0000-00-00"), "Дистанция не может быть меньше 1 км")

    def test_Too_Large_Distance(self):
        self.assertEqual(calculate_delivery_cost(10, 5001, "обычный"), (-1, "0000-00-00"), "Дистанция не может быть больше 5000 км")

    def test_Express_Should_Be_Expensive(self):
        self.assertEqual(calculate_delivery_cost(30, 100, "обычный", True), (2100, "2026-09-03"), "Экспресс доставка должна быть дороже обычной")

    def test_Invalid_Package_Type(self):
        self.assertEqual(calculate_delivery_cost(30, 100, "подозрительный"), (-1, "0000-00-00"), "Указан неверный тип пакета")

    def test_Dangerous_Package_Type(self):
        self.assertEqual(calculate_delivery_cost(30, 100, "опасный"), (2050, "2026-09-04"))

    def test_Little_Bit_Max_Weight(self):
        self.assertEqual(calculate_delivery_cost(50.01, 150, "обычный"), (-1, "0000-00-00"), "Вес не может быть больше 50.0 кг")

    def test_12_Weight_Coefficient(self):
        self.assertNotEqual(calculate_delivery_cost(12.0, 100, "обычный"), (-1, "0000-00-00"))

if __name__ == "__main__":
    unittest.main()