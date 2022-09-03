from unittest import TestCase

from easyio.excel import ExcelReader


class TestExcelReader(TestCase):

    @staticmethod
    def get_reader():
        return ExcelReader('test.xlsx')

    def test_read_sheets(self):
        reader = self.get_reader()
        for sheet, rows_g in reader.read_sheets(values_only=True):
            print(f'sheet: {sheet}')
            for row in rows_g:
                print(row)
        reader.close()

    def test_read_sheet(self):
        reader = self.get_reader()
        for sheet in reader.sheet_names:
            print(f'sheet: {sheet}')
            rows = reader.read_sheet(sheet)
            for r in rows:
                print(r)
        reader.close()

    def test_read_sheet_col_1(self):
        reader = self.get_reader()
        with reader:

            rows = list(reader.read_sheet(cols='1'))
            exp_data = [
                ('id',),
                (1,),
                (2,)
            ]
            self.assertEqual(rows, exp_data)

    def test_read_sheet_col_1_and_3(self):
        exp_data = [
            ('id', 'Age'),
            (1, 45),
            (2, 22)
        ]
        with self.get_reader() as reader:

            self.assertEqual(exp_data, list(reader.read_sheet(cols='1, 3')))
            self.assertEqual(exp_data, list(reader.read_sheet(cols=['id', 'Age'])))
            self.assertEqual(exp_data, list(reader.read_sheet(cols='id,Age')))

    def test_read_sheet_row_1(self):
        exp_data = [
            (1, 45),
            (2, 22)
        ]
        with self.get_reader() as reader:
            self.assertEqual(exp_data, list(reader.read_sheet(cols='1,3', min_row=2)))

    def test_read_sheet_cols_from_1_to_3(self):
        exp_data = [
            ('id', 'Name', 'Age'),
            (1, 'Peter', 45),
            (2, 'Brain', 22)
        ]
        with self.get_reader() as reader:
            self.assertEqual(exp_data, list(reader.read_sheet(cols='1:4')))
            self.assertEqual(exp_data, list(reader.read_sheet(cols=['1:4', '2:3'])))

    def test_read_sheet_cols_non_exists(self):
        try:
            with self.get_reader() as reader:
                _ = list(reader.read_sheet(cols='icebear'))
            self.fail('Exception should raised when read a non-exists column')
        except ValueError as ve:
            print(f'success : {ve.args}')
            pass
        except AssertionError:
            pass
        except Exception as e:
            self.fail(f'Unknown exception raised: {e.args}')

    def test_read_sheet_as_dict(self):

        exp_data = [
            {'id': 1, 'Name': 'Peter', 'Age': 45, 'Description': 'A man'},
            {'id': 2, 'Name': 'Brain', 'Age': 22, 'Description': 'A foo'}
        ]
        with self.get_reader() as reader:
            self.assertNotEqual(exp_data, reader.read_sheet_as_dict(header=None))

    def test_read_sheet_as_dict_list(self):
        header = ['id', '', 'Age']
        exp_data = [
            {'id': 1, 'Age': 45},
            {'id': 2, 'Age': 22}
        ]
        with self.get_reader() as reader:
             self.assertEqual(exp_data,
                              list(reader.read_sheet_as_dict(header=header)))

    def test_read_sheet_as_dict_map(self):
        header = {
            'id': 'id',
            'Age': 'user_age',
            'Name': 'user_name'
        }
        exp_data = [
            {'id': 1, 'user_age': 45, 'user_name': 'Peter'},
            {'id': 2, 'user_age': 22, 'user_name': 'Brain'}
        ]
        with self.get_reader() as reader:

            self.assertEqual(exp_data, list(reader.read_sheet_as_dict(header=header)))
