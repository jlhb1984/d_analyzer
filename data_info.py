import pandas as pd
import numpy as np
from units_report import Units_report

class Data_info:
    
    def __init__(self,table_info):
        self.info_table=table_info

    def info(table_info):
        df_table_info=pd.read_csv("./data/"+table_info)
        missing_data_count=df_table_info.isna().sum()
        print("\nDatos nulos: ")
        print(missing_data_count)
        print("\nInformacíón de la tabla: ")
        print(df_table_info.info())
        print("\nInformacíón estadística de la tabla: ")
        print(df_table_info.describe())
        total_rows=len(df_table_info)
        print("\nTotal de registros: ")
        print(total_rows)
        print("\nAgrupación de atributos: ")        
        #Seleccionar el atributo a buscar, en este caso es 'Event'.
        var_filter=input("Digita el atributo a analizar: ")
        df_value_counts=df_table_info[var_filter].value_counts()
        print(df_value_counts)
        exp_option=input("Deseas generar un reporte en formato csv?\nS/N\n")
        if exp_option=='S':
            Units_report.create_csv(df_value_counts,table_info+'_r') 
        #unique_elements, counts = np.unique(df_table_info, return_counts=True)
        #print("Unique elements: ",unique_elements)
        #print("Totales: ",counts)
        option_null=input("Deseas eliminar los datos nulos de la tabla?\nS/N \n")
        if option_null=="S":
            df_table_info.dropna(axis=0,inplace=True)
            print("\ndf_table_info: ")
            print(df_table_info.info())
            print(df_table_info)
            total_rows=len(df_table_info)