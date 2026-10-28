import unittest
from src.converter import Converter

class TestConverter(unittest.TestCase):
    def test_X_Is_Zero(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_X_Above_100_7(self):
        self.assertEqual(Converter.do(150.3), 1000)

    def test_X_Above_0(self):
        self.assertEqual(Converter.do(1.3), 1)

    def test_X_Below_0(self):
        self.assertEqual(Converter.do(-25.5), -30)

    def test_X_Below_Minus_30_5(self):
        self.assertEqual(Converter.do(-30.8), -2000)

    def test_Border_100_7(self):
        self.assertEqual(Converter.do(100.7), 1000)

    def test_Border_0(self):
        self.assertEqual(Converter.do(0.1), 0)

    def test_Border_Minus_30_4(self):
        self.assertEqual(Converter.do(-30.4), -35)

    def test_Border_Minus_30_5(self):
        self.assertEqual(Converter.do(-30.5), -2000)

if __name__ == '__main__':
    unittest.main()