from unittest import TestCase
from easyio.excel import ExcelReader


class TestExcelReader(TestCase):
    def test_read(self):
        reader = ExcelReader(file_path='test.xlsx')
        sheet_cols = {
            "Sheet1": "1:5",
            "Sheet2": "Book, Price"
        }
        for sheet in reader.read(sheet_cols=sheet_cols):
            sheet.print_sheet()

