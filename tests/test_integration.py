import unittest
from unittest.mock import Mock
from src.controller import Controller
from src.triangleDB import TriangleDB

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.db = TriangleDB(':memory:')
        self.ui = Mock()
        self.notifier = Mock()

        self.controller = Controller(self.ui, self.db, self.notifier)

    def tearDown(self):
        self.db.close()

    def test_Full_Scenario_Saves_To_Db_And_Notifies(self):
        self.ui.get_input.side_effect = [3, 4, 5]
        result_type, result_coords = self.controller.process()

        self.assertEqual(result_type, "Разносторонний")

        cached_data = self.db.get(3, 4, 5)
        self.assertIsNotNone(cached_data, "Данные должны сохраниться в БД")
        self.assertEqual(cached_data[0], "Разносторонний")

        self.notifier.send_result.assert_called_once_with("Разносторонний", result_coords)

    def test_Second_Call_Uses_Cache_And_Skips_Calculation(self):
        self.ui.get_input.side_effect = [10, 10, 10, 10, 10, 10]

        self.controller.process()
        self.notifier.send_result.reset_mock()

        result_type, _ = self.controller.process()

        self.assertEqual(result_type, "Равносторонний")
        self.notifier.send_result.assert_called_once()

        self.db.cursor.execute("SELECT COUNT(*) FROM triangle")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 1, "Повторный вызов не должен создавать дубликат в БД")

    def test_Invalid_Input_Isolates_Dependencies(self):
        self.ui.get_input.side_effect = [None, 5, 5]

        result_type, result_coords = self.controller.process()

        self.assertEqual(result_type, "")
        self.assertEqual(result_coords, [(-2, -2)] * 3)

        self.ui.show_result.assert_called_with("Некорректный ввод")

        self.notifier.send_result.assert_not_called()
        self.db.cursor.execute("SELECT COUNT(*) FROM triangle")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 0, "При ошибке ввода в БД ничего не пишется")

if __name__ == "__main__":
    unittest.main()