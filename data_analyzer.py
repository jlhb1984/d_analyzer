import pandas as pd
import numpy as np

class Data_analyzer:
    def __init__(self,number_plate):
        self.number_plate=number_plate

    def data_analysis(number_plate):
        print("data_analyzer01.")
        path='Historical_locations_'+number_plate+'.csv'
        print(path)

        #Carga del dataframe del vehículo.
        df_book=pd.read_csv(path)
        df_book.info()

        #Selección de los atributos mas significativos.
        df_book_filter01=df_book[['Unit','Events','Date','Landmark']]

        #Selección de los eventos mas significativos.
        df_book_land_pu=df_book_filter01[
            (df_book['Events']=='Geofence IN')|
            (df_book['Events']=='Geofence OUT')|
            (df_book['Events']=='Landmark IN') |
            (df_book['Events']=='Landmark OUT')|
            (df_book['Events']=='POWER UP')|
            (df_book['Events']=='Ignition ON')]
            #print(df_book_land_pu)

        #Aquí irá los valores del atributo estudiado del dataframe del vehículo.
        landmarks=df_book_land_pu.loc[:,'Landmark']
        print("Landmarks info: ")
        #print(landmarks)

        #Elimino los registros duplicados para el atributo estudiado.
        landmarks.drop_duplicates(inplace=True)
        #print(landmarks)
        #print("Total de registros: ",landmarks.count())

        #Creo la lista de geofences:
        df_book_geofences=pd.read_csv('Geofences InOut Report.csv')
        df_book_geofences_GeofenceName=df_book_geofences['GeofenceName']
        df_book_geofences_GeofenceName.drop_duplicates(inplace=True)
        #print(df_book_geofences_GeofenceName.head(2))
        geofences=df_book_geofences_GeofenceName
        total_geofences=geofences.count()
        print("Total geofences: ",total_geofences)

        print("Wrong logs: ")

        for i in range(0,total_geofences):                
                wrong_logs=df_book_land_pu[
                ((df_book_land_pu['Events']=='Landmark OUT')&
                 (df_book_land_pu['Landmark']==geofences.iloc[i])|
                 (df_book_land_pu['Events']=='Landmark IN')&
                 (df_book_land_pu['Landmark']==geofences.iloc[i])
                )
                ]
                    
                if len(wrong_logs)!=0:
                    print(wrong_logs)
