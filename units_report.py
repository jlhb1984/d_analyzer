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
        print("\nSelecciona 4 atributos de la tabla:")
        for i in range (0,4):
             attributes.append(input("\nDigita el nombre del atributo: "))        
        df_book_filter01=df_books[[attributes[0],attributes[1],attributes[2],attributes[3]]]
        print(df_book_filter01)               
        exp_option=input("Deseas generar un reporte en formato csv?\nS/N\n")
        if exp_option=='S':
             var_filter='Filtered_report'             
             Units_report.create_csv(df_book_filter01,var_filter)
        null_values=input("Desea hacer tratamiento de datos faltantes: ")
        if null_values=='S':
             print("Datos null: ")
             print(df_book_filter01.isnull())
             print("Datos na: ")
             print(df_book_filter01.isna())
             print("Datos faltantes totales: ")
             print(df_book_filter01.missing.number_complete())

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
        