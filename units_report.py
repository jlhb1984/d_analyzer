import pandas as pd
import numpy as np

class Units_report:
    
    def __init__(self,table_name):
        self.table_name=table_name

    def create_report(table_name):
        df_books=pd.read_csv("./data/"+table_name)        
        df_books.info()
        #num_attribute=int(input("Digita el número de atributos a buscar: "))
        attributes=[]
        print("\nSelecciona 4 atributos de la tabla:")
        for i in range (0,4):
            attributes.append(input("\nDigita el nombre del atributo: "))        
        df_book_filter01=df_books[[attributes[0],attributes[1],attributes[2],attributes[3]]]
        print(df_book_filter01)        
        null_values=input("Desea hacer tratamiento de datos faltantes?\nS/N\n")
        if null_values=='S':
            print("Datos null: ")
            print(df_book_filter01.isnull())
            print("Datos na: ")
            print(df_book_filter01.isna())
            print("Datos faltantes totales: ")
            print(df_book_filter01.isnull().sum())            
            """
            Pairwise deletion: Al hacer operaciones matemáticas pandas omite los valores faltantes.
            .mean(skipna=False) para tener en cuenta los valores faltantes.
            Listwise deletion:
            how=all, si es requerido eliminar toda la dila si todos los atributos son null.
            how=any, si es requerido eliminar toda la fila si almenos un atributo es null.
            Las siguientes instrucciones no funcionaron, quizá porque no está la librería janitor.
            df_book_filter01.dropna(subset=['Phone Number'],how="any")
            print("Data_frame tratado (how=any):")
            print(df_book_filter01.info())

            """            
            df_book_filter01.dropna(axis=0,inplace=True)
            print("Data_frame tratado (dropna)")
            print(df_book_filter01.info())
            print(df_book_filter01.isnull().sum())

        #imput_=input()
        
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
        filter_df.to_csv("./reports/"+look_word+'.csv')
        