import pandas as pd
import numpy as np

class Tables_comparator:
    def __init__(self,df_book_table01,df_book_table02):
        self.df_book_table01=df_book_table01
        self.df_book_table02=df_book_table02
             
    def comparator(df_book_table01,df_book_table02):
        num_filas_table01=int(df_book_table01.shape[0])
        num_filas_table02=int(df_book_table02.shape[0])

        print("Trabajando...")
        cont=0
        df_aux=pd.DataFrame()
        lista_simcard=[]
        lista_linea=[]
                  
        for i in range(0,num_filas_table01):
            for j in range(0,num_filas_table02):                
                if df_book_table01.iloc[i,0]==df_book_table02.iloc[j,5]:                   
                    lista_simcard.append(df_book_table02.iloc[j,5])
                    lista_linea.append(df_book_table02.iloc[j,3])
                    cont=cont+1
        df_aux['SIMCARD']=lista_simcard
        df_aux['LINEA']=lista_linea
        print("Cont= ",cont)
        print(df_aux.info())
        option_exp=input("\n¿Desea generar un reporte en formato csv S/N?\n")
        if option_exp=="S":
            df_aux.to_csv('tables_comparator.csv')
        #lista_combinada=[lista_simcard,lista_linea]
       
              
                    