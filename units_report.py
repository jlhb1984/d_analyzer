import pandas as pd
import numpy as np

class Units_report:
    def __init__(self,table_name):
        self.table_name=table_name

    def create_report(table_name):
        df_books=pd.read_csv(table_name)        
        df_books.info()
        #num_attribute=int(input("Digita el número de atributos a buscar: "))
        attributes=[]
        print("\nBuscar 3 atributos de la tabla:")
        for i in range (0,4):
             attributes.append(input("\nDigita el atributo a buscar: "))        
        #En la siguiente línea se puefe agregar los atributos a visualizar, si es uno, no modificar el código.
        #df_book_filter01=df_books[[var_filter]]#,'Unit ID','Unit Type','Phone Number','Sim Number','IMEI','Last Event Date']]
        df_book_filter01=df_books[[attributes[0],attributes[1],attributes[2],attributes[3]]]
        print(df_book_filter01) 
        #print(df_book_filter01[var_filter].value_counts())
        #df_book_filter01.dropna(axis=0,inplace=True)        
        exp_option=input("Deseas generar un reporte en formato csv?\nS/N\n")
        if exp_option=='S':
             var_filter='Filtered_report'             
             Units_report.create_csv(df_book_filter01,var_filter)

        look_option=input("¿Deseas buscar una unidad del atributo?\nS/N\n")
        if look_option=='S':
                var_filter=input("Digita el atributo a explorar: ")
                #Se agregó: df_book_filter01[var_filter]=df_book_filter01[var_filter].astype(str)
                df_book_filter01[var_filter]=df_book_filter01[var_filter].astype(str)                
                Units_report.look_for(df_book_filter01,var_filter,look_option)

    def look_for(df_book_filter01,var_filter,look_option):        
        look_word="w"        
        while look_option!='N':                                               
                look_word=input("Digita la unidad a buscar: ")
                #look_word_aux=str(look_word)
                filter_df=df_book_filter01[df_book_filter01[var_filter].str.contains(look_word)]
                print("Report of units "+look_word+":")
                print(filter_df)
                look_option=input("Deseas buscar una unidad:\nS/N\n")
        exp_option=input("Deseas generar un reporte en formato csv?\nS/N\n")
        if exp_option=='S':
             Units_report.create_csv(filter_df,look_word)

    def create_csv(filter_df,look_word):
        filter_df.to_csv(look_word+'.csv')
        