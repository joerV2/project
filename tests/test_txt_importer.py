
import tempfile
import unittest

from pathlib import Path
from src.txt_importer import import_txt


class TestTxtImporter(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_import_txt(self):
        file = self.folder / "test.txt"
        file.write_text("Вопрос: Тест\nОтвет: Проверка", encoding="utf-8")

        result = import_txt(file)

        self.assertEqual(result, "Вопрос: Тест\nОтвет: Проверка")

    def test_empty_file(self):
        file = self.folder / "empty.txt"
        file.write_text("", encoding="utf-8")

        with self.assertRaises(ValueError):
            import_txt(file)

    def test_wrong_extension(self):
        file = self.folder / "test.pdf"
        file.write_text("Тест", encoding="utf-8")

        with self.assertRaises(ValueError):
            import_txt(file)

    def test_missing_file(self):
        file = self.folder / "missing.txt"

        with self.assertRaises(FileNotFoundError):
            import_txt(file)


if __name__ == "__main__":
    unittest.main()
