schema_template = {
    "load_dag_id": "load_to_bq_dag",
    "target_type": "BIGQUERY",
    "target_spec":{
        "table":'', #<<excel_filename>>
        "schema":'', #<<schema_from_file>> list of dictinaries
        "dataset": '',
        "region_bq": "Australia",
        "big_queryview": '', #V_<<excel_filename>>
        "big_query_temp_table": '' #T_<<excel_filename>>
    }
}

 