# easyio

A set of tools to handle file input/output like excel, txt, csv, etc.

## Read excel

**Assume you have a xlsx file like this:**

`Sheet1`

| id  | Name  | Age | Description |
|-----|-------|-----|-------------|
| 1   | Peter | 45  | A man       |
| 2   | Brain | 22  | A foo       |

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
with reader:
    for sheet, rows_g in reader.read_sheets(values_only=True):
        print(f'sheet: {sheet}')
        for row in rows_g:
            print(row)
```

- Output:

```text
sheet: Sheet1
('id', 'Name', 'Age', 'Description')
(1, 'Peter', 45, 'A man')
(2, 'Brain', 22, 'A fool')
sheet: Sheet2
('Book', 'Price', 'Location')
('To kill a mocking bird', '$9.9', 'Level-2-rack-1')
('Python cookbook', '$12.9', 'Level-1-rack-2')
```

- If you want to print specific sheet:

```python
with reader:
    for row in reader.read_sheet('Sheet1'):
        print(row)
```

- Output:

```text
('id', 'Name', 'Age', 'Description')
(1, 'Peter', 45, 'A man')
(2, 'Brain', 22, 'A fool')
```

- Specific the col you want to read:

```python
with reader:
    for row in reader.read_sheet('Sheet1', cols=['id', 'Name']):
        print(row)

    # You can also specify cols by str like:
    for row in reader.read_sheet('Sheet1', cols='id,Name'):
        ...

    # or with range(1-based, 1:3 means from column 1 to column 2):
    for row in reader.read_sheet('Sheet1', cols='1:3'):
        ...

    # or just specify the column index(1-based)
    for row in reader.read_sheet('Sheet1', copls='1,2'):
        ...
```

- Output:

```text
('id', 'Name')
(1, 'Peter')
(2, 'Brain')
```

**Sometime, you do not want to read a xlsx-file with a list of tuples returned, you may want to get a list of dicts.**

- Return rows as list[dict] format

```python
with reader:
    for row in reader.read_sheet_as_dict():
        print(row)
```

- Output:

```text
{'id': 1,'Name': 'Peter', 'Age': 45, 'Description': 'A man'}
......
```

- You can also specify the headers

```python
with reader:
    for row in reader.read_sheet_as_dict(
        header={
            'id': 'id',
            'Name': 'user_name',
            'Age': 'user_age',
            'Description': 'desc'
        }
    ):
        print(row)

```

- Output:

```text
{'id': 1, 'user_name': 'Peter', 'user_age': 45, 'desc': 'A man'}
```

- There are 3 ways to specify header when you want to return a list of dicts:

    - None: If header is None, the **first row** will be regarded as header
    - list[str]: A list of string. eg: `header = ['id', '', 'Name']` will read column1 and column3, and ignore column 2
    - dict[str, str]: A map of xlsx-file-header: header-you-want. eg: `header = {'Name':'user_name'}` will only read column `Name` and return with {user_name: ...}
 
