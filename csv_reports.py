import pandas as pd

#table_name=input("\nDigita el nombre de la tabla 1:")
#df=pd.read_csv(table_name)

def csv_reports(df):
       df_unit_types=df[['Unit Type','IMEI','Company','Phone Number','Last Event Date']]
       print(df_unit_types)
       exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
       if (exp_option=="S"):
            df_unit_types.to_csv('Unit_searched_report_units.csv')

            look_option=input("Desea buscar una unidad:\nS/N\n")
            while look_option!='N':
                look_word=input("Digita la unidad a buscar: ")
                filter_df=df_unit_types[df_unit_types['Unit Type'].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Desea buscar una unidad:\nS/N\n")

            exp_option=input("Desea generar un archivo en formato csv?\nS/N\n")
            if (exp_option=="S"):
                filter_df.to_csv('Unit_searched_report_units.csv')  