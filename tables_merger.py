import pandas as pd
import numpy as np
from units_report import Units_report

class Tables_merger:
    
    def __init__(self,number_of_tables):
        self.number_of_tables=number_of_tables
            
    def merger(number_of_tables):       
               
        if number_of_tables==1:
             print("No tiene sentido fusionar 1 tabla.")
           
        elif number_of_tables>1:
            table_name=input("\nDigita el nombre de la tabla 1: ")
            df=pd.read_csv("./reports/"+table_name)
            print("Información del dataframe: ")
            print(df.info())

            #            df_unit_types=df[['Date','Speed','Send Time','Mileage']]
            attributes=[]
            print("\nSelecciona 4 atributos de la tabla:")

            for i in range (0,4):
                        attributes.append(input("\nDigita el nombre del atributo: "))
            df_unit_types=df[[attributes[0],attributes[1],attributes[2],attributes[3]]]
                                    
            for i in range(1,number_of_tables):                
                table_name=input("\nDigita el nombre de la tabla: ")
                df_aux=pd.read_csv("./reports/"+table_name)
                df_aux_unit_types=df_aux[[attributes[0],attributes[1],attributes[2],attributes[3]]]
                print("\nUnite types before concat:")
                print("\n")
                print(df_unit_types.info())                
                df_unit_types=pd.concat([df_unit_types,df_aux_unit_types],axis=0)
                print("\nUnite types after concat:")
                print("\n")
                print(df_unit_types.info())
                
            option_null=input("Desea eliminar los datos nulos de la tabla: S/N \n")
            if option_null=="S":
                df_unit_types.dropna(axis=0,inplace=True)
                print("df_table_info: ")
                print(df_unit_types.info())
                print(df_unit_types) 
            
            Tables_merger.csv_reports(df_unit_types)           

    def csv_reports(df_unit_types):       
        df_unit_types
        print(df_unit_types)
        exp_option=input("Desea generar un reporte en formato csv?\nS/N\n")
        if (exp_option=="S"):
                df_unit_types.to_csv('./reports/Units_report.csv')