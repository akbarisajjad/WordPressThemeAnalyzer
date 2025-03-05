import unittest
import os
import shutil
from main_analyzer import WordPressThemeAnalyzer

class TestWordPressThemeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.theme_path = "test_theme"
        os.makedirs(self.theme_path, exist_ok=True)

    def test_validate_theme_path(self):
        analyzer = WordPressThemeAnalyzer(self.theme_path)
        self.assertTrue(analyzer.validate_theme_path())

    def tearDown(self):
        shutil.rmtree(self.theme_path)

if __name__ == "__main__":
    unittest.main()
