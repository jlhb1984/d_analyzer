import pandas as pd
import numpy as np
from tables_comparator import Tables_comparator
from data_analyzer import Data_analyzer
from units_report import Units_report
from tables_merger import Tables_merger
from data_info import Data_info
from date import Date
from imei_phone_filter import Imei_phone_filter
from chart import Chart

print("data_analyzer.")
option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Filtered report. \n4. Merger. \n5. Table_info. \n6. Messages. \n7. Str_date_order. \n8. Gráficos.  \n9. Salir. \n")

while option!='9':
    
    if option=='1':
        number_plate=input("\nDigite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)

    elif option=='2':
        table01=input("\nDigita el nombre de la tabla 1: ")
        df_book_table01=pd.read_csv(table01)
        
        table02=input("\nDigita el nombre de la tabla 2: ")
        df_book_table02=pd.read_csv(table02)

        Tables_comparator.comparator(df_book_table01,df_book_table02)

    elif option=='3':
        #Carga de la tabla. Customer-Units.csv
        table_name=input("\nDigita el nombre de la tabla: ")
        Units_report.create_report(table_name)

    elif option=='4':
        #carga de las tablas a fusionar.
        number_of_tables=int(input("\nDigita el número de tablas: "))
        Tables_merger.merger(number_of_tables)

    elif option=='5':
        table_info=input("\nDigita el nombre de la tabla: ")
        Data_info.info(table_info)
    
    elif option=='6':
        message=input("\nDigita la cadena: ")
        print("\nLongitud de la cadena: ",len(message))

    elif option=='7':
        table02=input("Digita el nombre de la tabla: ")
        Date.order_date(table02)

    elif option=='8':
        graph_option=input("Numero de tablas: \n1./2: ")
        if graph_option=='1':
            data_table=pd.read_csv('Searched_unit_report.csv')
            Chart.chart_time_1(data_table)            

        elif graph_option=='2':
            time=pd.read_csv('Date_ordered.csv')
            print(time.info())
            values=pd.read_csv('Event.csv')
            print(values.info())
            Chart.chart_time_2(time,values)          
  
    elif option=='9':
        print("Saliendo")
        break
    
    option=input("\n1. Data_analyzer01.\n2. Tables comparator.\n3. Filtered report. \n4. Merger. \n5. Table_info. \n6. Messages. \n7. Str_date_order. \n8. Gráficos. \n9. Salir. \n")
