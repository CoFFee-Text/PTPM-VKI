import unittest
from src.forumParser import ForumParser

class TestForumParser(unittest.TestCase):
    def setUp(self):
        self.parser = ForumParser()
        with open("tests/file/html_file.html", "r", encoding="utf-8") as f:
            self.html = f.read()

    def test_Html_Returns_Not_Empty_List(self):
        items = self.parser.parse_html(self.html)
        self.assertGreater(len(items), 0)

    def test_Html_Item_Fields(self):
        items = self.parser.parse_html(self.html)
        first = items[0]
        self.assertIsInstance(first["id"], int)
        self.assertTrue(first["name"])
        self.assertTrue(first["message"])
        self.assertGreater(first["id"], 0)

    def test_Html_Unique_Id(self):
        items = self.parser.parse_html(self.html)
        ids = [item["id"] for item in items]
        self.assertEqual(len(ids), len(set(ids)), "ID должны быть уникальны")