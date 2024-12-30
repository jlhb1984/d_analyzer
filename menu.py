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
from joins import Joins
import json

print("data_analyzer.")
print("\n1. Data_analyzer01.\n2. Units report.\n3. Tables comparator.\n4. Merger.",end="")
print("\n5. Table_info. \n6. Messages. \n7. Str_date_order. \n8. Charts. \n9. Joins.")
print("10. json to dataframe.\n11. Exit.")
option=input()

while option!='11':
    
    if option=='1':
        number_plate=input("\nDigite la placa del vehículo en mayúscula: ")
        print(number_plate)
        Data_analyzer.data_analysis(number_plate)
        pass

    elif option=='2':
        #Carga de la tabla. Customer-Units.csv
        table_name=input("\nDigita el nombre de la tabla: ")
        Units_report.create_report(table_name)
        pass        

    elif option=='3':
        table01=input("\nDigita el nombre de la tabla 1 desde reports, (pasar por opción 2 previamente): ")
        df_book_table01=pd.read_csv("./reports/"+table01)        
        table02=input("\nDigita el nombre de la tabla 2 desde reports, (Pasar por opción 2 previamente): ")
        df_book_table02=pd.read_csv("./reports/"+table02)
        Tables_comparator.comparator(df_book_table01,df_book_table02)
        pass       

    elif option=='4':
        #carga de las tablas a fusionar.
        number_of_tables=int(input("\nDigita el número de tablas: "))
        Tables_merger.merger(number_of_tables)
        pass

    elif option=='5':
        table_info=input("\nDigita el nombre de la tabla: ")
        Data_info.info(table_info)
        pass
    
    elif option=='6':
        message=input("\nDigita la cadena: ")
        print("\nLongitud de la cadena: ",len(message))
        pass

    elif option=='7':
        table02=input("Digita el nombre de la tabla: ")
        Date.order_date(table02)
        pass

    elif option=='8':
        graph_option=input("Número de tablas: \n1./2: ")
        if graph_option=='1':
            data_table=pd.read_csv("./reports/info.csv")
            Chart.chart_time_1(data_table)
        elif graph_option=='2':
            time=pd.read_csv('Date_ordered.csv')
            print(time.info())
            values=pd.read_csv('Event.csv')
            print(values.info())
            Chart.chart_time_2(time,values)
        pass

    elif option=='9':
        print("Developing...")
        table01=input("\nDigita el nombre de la tabla 1 (por lo menos 1 atributo): ")
        df_book_table01=pd.read_csv(table01)        
        table02=input("\nDigita el nombre de la tabla 2 (Pasar por opción 2 previamente): ")
        df_book_table02=pd.read_csv(table02)
        Joins.inner_join(table01,table02)
        pass
  
    elif option=='10':
        file_name=input("\Digita el nombre del archivo: ")

        with open(file_name, mode='r') as f:
            data = json.load(f)            
        df = pd.DataFrame(data)
        df.to_csv("json_csv.csv")
        print(df)        
        pass
    
    print("\n1. Data_analyzer01.\n2. Units report.\n3. Tables comparator.\n4. Merger.",end="")
    print("\n5. Table_info. \n6. Messages. \n7. Str_date_order. \n8. Charts. \n9. Joins.")
    print("10. json to dataframe.\n11. Exit.")
    option=input()
 