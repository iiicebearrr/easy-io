# easyio

A set of tools to handle file input/output like excel, txt, csv, etc.

## Read excel

**Assume you have a xlsx file like this:**

`Sheet1`

| id  | Name  | Age |
|-----|-------|-----|
| 1   | Peter | 45  |
| 2   | Brain | 22  |

`Sheet2`

| Book                   | Price | Location       |
|------------------------|-------|----------------|
| To kill a mocking bird | $9.9  | Level-2-rack-1 |
| Python cookbook        | $12.9 | Level-1-rack-2 |

- Then if you want to read all sheets:

```python
from easyio import ExcelReader

# Path to xlsx file
xlsx_file_path = 'easyio/excel/tests/test.xlsx'

reader = ExcelReader(xlsx_file_path)

# Print all sheets rows
for sheet, rows_g in reader.read_sheets(values_only=True):
    print(f'sheet: {sheet}')
    for row in rows_g:
        print(row)
```

- Output:

```text
sheet: Sheet1
('id', 'Name', 'Age')
(1, 'Peter', 45)
(2, 'Brain', 22)
sheet: Sheet2
('Book', 'Price', 'Location')
('To kill a mocking bird', '$9.9', 'Level-2-rack-1')
('Python cookbook', '$12.9', 'Level-1-rack-2')
```

- If you want to print specific sheet:

```python
for row in reader.read_sheet('Sheet1'):
    print(row)
```

- Output:

```text
('id', 'Name', 'Age')
(1, 'Peter', 45)
(2, 'Brain', 22)
```

- Specific the col you want to read:

```python
for row in reader.read_sheet('Sheet1', cols=['id', 'Name']):
    print(row)

# You can also specify cols by str like:
for row in reader.read_sheet('Sheet1', cols='id,Name'):
    ...

# or with range(1-based, 1:3 means from column 1 to column 2):
for row in reader.read_sheet('Sheet1', cols='1:3'):
    ...

# or with numeric 
for row in reader.read_sheet('Sheet1', copls='1,2'):
    ...
```

- Output:

```text
('id', 'Name')
(1, 'Peter')
(2, 'Brain')
```