# prototype xlsx to YAML for metadata
import xlrd
import json
import yaml
import os


def replace_file_name_in_template(input_excel_name):
    return(file_name.split('.')[0] + '.yaml')
    


#get the excel filename
base_path = '../template'
file_name = 'Metadata_JSON_Build_v1.xlsx'
input_excel_name = ("/").join([base_path, file_name])


output_yaml_name = replace_file_name_in_template(input_excel_name)

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(input_excel_name)
sheet = wb.sheet_by_index(0)



cols = [] # attaributes from the header row - has to ordered so cannot keep it as a dictionary
# cols = {}
for i in sheet.row_values(0):
    cols.append(i)
    # cols.update( {i : ""} )
print()
print("print the schema***\n")
# print(cols)
for i in cols:
    print(i)


schema= ""
for rownum in range(1, sheet.nrows):
    row_values = sheet.row_values(rownum)
    d ={}
    for i  in range(len(cols)):
        d.update({cols[i]:row_values[i]})
        schema += str(d) + ','
# print(schema)
#strip the last comma
schema = schema.rstrip(',')


# keep adding the row values to the schema
temp_yaml = []
with open('../template/schema_template.txt','r') as infile:
    with open('temp.txt','w') as outfile:
        pattern = infile.read()
        string_replace = pattern.replace("<<excel_filename>>",file_name.split('.')[0])
        string_replace = string_replace.replace("<<table_schema>>",schema)
        outfile.write(string_replace)

# Serialize to YAML
with open('temp.txt','r') as infile:
    contents = infile.read()

yaml_contents=yaml.dump(contents)

with open(output_yaml_name,'w') as outfile:
    outfile.write(yaml_contents)
