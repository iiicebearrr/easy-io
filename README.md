# easyio

A set of tools to handle file input/output like excel, txt, csv, etc.

## Read excel

- Assume you have a xlsx file like this:

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

- Then you want to read all sheets:

```python
from easyio import ExcelReader

# Path to xlsx file
xlsx_file_path = 'easyio/excel/tests/test.xlsx'

reader = ExcelReader(xlsx_file_path)

for sheet in reader.read():
    # print sheet name and sheet rows
    print(f'sheet: {sheet.sheet_name}')
    for row in sheet.sheet_rows:
        print(f'row: {row}')

    # Or you can just call sheet.print_sheet() to get a better preview of content
    # sheet.print_sheet()
```

- Output:

```text
sheet: Sheet1
row: ('id', 'Name', 'Age')
row: (1, 'Peter', 45)
row: (2, 'Brain', 22)
sheet: Sheet2
row: ('Book', 'Price', 'Location')
row: ('To kill a mocking bird', '$9.9', 'Level-2-rack-1')
row: ('Python cookbook', '$12.9', 'Level-1-rack-2')
```

- Output(`sheet.print_sheet()`)

```text
----------------------Sheet1----------------------
| [0]: ('id', 'Name', 'Age')
| [1]: (1, 'Peter', 45)
| [2]: (2, 'Brain', 22)
----------------------Sheet2----------------------
| [0]: ('Book', 'Price', 'Location')
| [1]: ('To kill a mocking bird', '$9.9', 'Level-2-rack-1')
| [2]: ('Python cookbook', '$12.9', 'Level-1-rack-2')
```