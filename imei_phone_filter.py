import pandas as pd
import numpy as np

class Imei_phone_filter:
    def __init__(self,df_table_info,total_rows):
        self.df_table_info=df_table_info
        self.total_rows=total_rows

    def imei_phone_len_filter(df_table_info,total_rows):
        number_of_chars_pn=int(input("\nDigita el número de caracteres a detectar en el campo Phone Number: \n"))
        for i in range(0,total_rows):
            if len(str(df_table_info.iloc[i]['Phone Number']))<number_of_chars_pn:
                print("\nSe encontró registros Phone Number con longitud inferior a la buscada.\n")
                print(df_table_info.iloc[i])
                #df_phone_number=df_table_info.iloc[i]
        number_of_chars_im=int(input("\nDigita el número de caracteres a detectar en el campo IMEI: \n"))
        for j in range(0,total_rows):
            if len(str(df_table_info.iloc[j]['IMEI']))<number_of_chars_im:
                print("\nSe encontró registros IMEI con longitud inferior a la buscada.\n")
                print(df_table_info.iloc[j])
                #df_imei=df_table_info.iloc[j]
        option_drop=input("\nDeseas eliminar los registros que no cumplen la cantidad de caracteres requeridos: S/N \n")
        if option_drop=='S':
            print(total_rows)
            print(df_table_info.info()) 
            df_table_info_aux=df_table_info
           
            for i in range(0,total_rows):
                if len(df_table_info.iloc[i]['Phone Number'])<number_of_chars_pn:
                    df_table_info_aux=df_table_info_aux.drop(i)
            #df_table_info=df_table_info_aux
            total_rows=len(df_table_info_aux)
            df_table_info_aux_f=df_table_info_aux
            for i in range(0,total_rows):
                if (len(str(df_table_info_aux.iloc[i]['IMEI'])))<number_of_chars_im:
                    df_table_info_aux_f=df_table_info_aux_f.drop(i)
                print(df_table_info_aux_f.info())
        elif option_drop=='N':
            print("OK!")