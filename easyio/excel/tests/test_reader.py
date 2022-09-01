from unittest import TestCase

from easyio.excel import ExcelReader


class TestExcelReader(TestCase):
    def test_read_all(self):
        reader = ExcelReader(file_path='test.xlsx')
        for sheet, rows_g in reader.read_sheets(values_only=True):
            print(f'sheet: {sheet}')
            for row in rows_g:
                print(row)

    def test_read_as_dict(self):
        reader = ExcelReader(file_path='test.xlsx')
        test_headers = [
            None,
            ['id', '', 'Age'],
            {
                'id': 'ID',
                'Name': 'NAME'
            }
        ]
        for header in test_headers:
            for row in reader.read_sheet_as_dict(header=header):
                print(row)
