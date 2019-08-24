# prototype xlsx to YAML for metadata
import xlrd
import yaml
import os


schema_template = {
    "load_dag_id": "load_to_bq_dag",
    "target_type": "BIGQUERY",
    "target_spec":{
        "table":'', #<<excel_filename>>
        "schema":[], #<<schema_from_file>>
    "dataset": '',
    "region_bq": "Australia",
    "big_queryview": '', #V_<<excel_filename>>
    "big_query_temp_table": '' #T_<<excel_filename>>
    }
}


def replace_file_name_in_template(input_excel_name):
    return(file_name.split('.')[0])
    


#get the excel filename
base_path = '../template'
file_name = 'Metadata_JSON_Build_v1.xlsx'
input_excel_name = ("/").join([base_path, file_name])


output_yaml_name = replace_file_name_in_template(input_excel_name)
table_schema = schema_template

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook(input_excel_name)
sheet = wb.sheet_by_index(0)



cols = [] # attributes from the header row - has to ordered so cannot keep it as a dictionary
for i in sheet.row_values(0):
    cols.append(i)
print()

#column names and type
schema= []
for rownum in range(2, sheet.nrows):
    row_values = sheet.row_values(rownum)
    d ={}
    for i  in range(len(cols)):
        d[cols[i]]=row_values[i]
    schema.append(d)

table_schema['target_spec']['schema'].append(schema)
table_schema['target_spec']['table'] = output_yaml_name
table_schema['target_spec']['dataset'] = output_yaml_name
table_schema['target_spec']['big_queryview'] = "V_"+output_yaml_name
table_schema['target_spec']['big_query_temp_table'] = "T_"+output_yaml_name


yaml_contents=yaml.dump(table_schema)

with open(output_yaml_name+".yaml",'w') as outfile:
    outfile.write(yaml_contents)