# prototype xlsx to json format for ARC framework
import xlrd
import json
import uuid

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('somesamplefile.xlsx')
sheet = wb.sheet_by_index(0)

out_json = "meta_somesamplefile.json"

cols = [] # attaributes from the header row - has to ordered so cannot keep it as a dictionary
for i in sheet.row_values(0):
    cols.append(i)
print()
print("print the schema***\n")
for i in cols:
    print(i)


# keep adding the row values to the schema
jason = []
guid = ""
for rownum in range(1, sheet.nrows):
    row_values = sheet.row_values(rownum)
    guid = str(uuid.uuid4())
    d = {

        "id": guid,
        "trim" : bool("true")
        }
    for i  in range(len(cols)):
        if cols[i] == 'Key':
            continue
        if cols[i] == 'IS_NULLABLE':
            d.update({cols[i]:bool(row_values[i])})
        else:
            d.update({cols[i]:row_values[i]})

    jason.append(d)

# Serialize the list of dicts to JSON
j = json.dumps(jason)
# Write to file
#with open('data.json', 'w') as f:
with open(out_json,'w') as f:
    f.write(j)
    
    """
    Sample output
    [
    {
        "id": "7a42bd87-9986-4ef8-8b04-a0c1350b287c",
        "trim": true,
        "COLUMN_NAME": "HouseNum1",
        "IS_NULLABLE": true,
        "DATA_TYPE": "numeric",
        "CHARACTER_MAXIMUM_LENGTH": "NULL",
        "NUMERIC_PRECISION": 5.0,
        "NUMERIC_PRECISION_RADIX": 10.0,
        "NUMERIC_SCALE": 0.0
    },
    {
        "id": "e1289989-f741-47b9-9285-4b5b6debcd53",
        "trim": true,
        "COLUMN_NAME": "HouseNumSuffix1",
        "IS_NULLABLE": true,
        "DATA_TYPE": "varchar",
        "CHARACTER_MAXIMUM_LENGTH": 1.0,
        "NUMERIC_PRECISION": "NULL",
        "NUMERIC_PRECISION_RADIX": "NULL",
        "NUMERIC_SCALE": "NULL"
    },
    {
        "id": "37f44de8-fae8-4572-87e5-5996f26f5636",
        "trim": true,
        "COLUMN_NAME": "StreetSuffix1",
        "IS_NULLABLE": true,
        "DATA_TYPE": "varchar",
        "CHARACTER_MAXIMUM_LENGTH": 2.0,
        "NUMERIC_PRECISION": "NULL",
        "NUMERIC_PRECISION_RADIX": "NULL",
        "NUMERIC_SCALE": "NULL"
    }
    ]
    """


