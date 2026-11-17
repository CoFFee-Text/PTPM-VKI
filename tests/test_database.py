import unittest
import sqlite3

from src.commentsDb import DatabaseRepository

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.repo = DatabaseRepository(':memory:')

    def tearDown(self):
        self.repo.close()
    # add
    def test_Add_Success(self):
        self.assertTrue(self.repo.add(1, 'testovich', 'aaaa, ponyatno'))

    def test_Add_Negative_Duplicate(self):
        self.repo.add(1, 'test1', 'chto-to')
        with self.assertRaises(sqlite3.IntegrityError):
            self.repo.add(1, 'test2', 'ya ustal')

    def test_Add_Very_Long_Name(self):
        with self.assertRaises(ValueError):
            self.repo.add(1, 'a' * 257, 'aa')

    def test_Add_Very_Long_Message(self):
        self.repo.add(1, 'testik', 'testovoe soobshchenie kraine interesnoe')
        with self.assertRaises(ValueError):
            self.repo.update(1, 'a' * 8097)

    def test_Add_Empty_Name(self):
        with self.assertRaises(ValueError):
            self.repo.add(1, '', 'aa')

    #update
    def test_Update_Success(self):
        self.repo.add(1, 'testovich', 'aaaa, ponyatno')
        self.assertTrue(self.repo.update(1, "new message"))

    def test_Update_Nonexistent_User(self):
        self.assertFalse(self.repo.update(666, 'new'))

    def test_Update_Very_Long_Message(self):
        self.repo.add(1, 'testik', 'testovoe soobshchenie kraine interesnoe')
        with self.assertRaises(ValueError):
            self.repo.update(1, 'a' * 8097)

    def test_Update_Empty_Message(self):
        with self.assertRaises(ValueError):
            self.repo.update(1, '')

    #delete
    def test_Delete_Success(self):
        self.repo.add(1, 'testovich', 'aaaa, ponyatno')
        self.assertTrue(self.repo.delete(1))

    def test_Delete_Nonexistent_Id(self):
        self.assertFalse(self.repo.delete(665))

    #get_by_id
    def test_Get_By_Id_Success(self):
        self.repo.add(1, 'testovich', 'aaaa, ponyatno')
        self.assertEqual((self.repo.get_by_id(1)), {'id': 1, 'message': 'aaaa, ponyatno', 'name': 'testovich'})

    def test_Get_By_Id_Nonexistent_Id(self):
        self.assertIsNone(self.repo.get_by_id(777))

    #get_by_name
    def test_Get_By_Name_Success(self):
        self.repo.add(1, 'testovich', 'aaaa, ponyatno')
        self.assertTrue((self.repo.get_by_name('testovich')))

    def test_Get_By_Name_Nonexistent_Name(self):
        self.repo.add(1, 'testovich', 'aaaa, ponyatno')
        self.assertEqual(self.repo.get_by_name('testov123'), [])

if __name__ == "__main__":
    unittest.main()