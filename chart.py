import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Chart:

    def __init__(self,time,values):
        self.time=time
        self.values=values

    def chart_time_2(time,values):
        #Crear Gráfico de líneas
        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(time['Time'], values['Event'], color = 'green')        
        plt.xticks(rotation=90)
        plt.title('Serie de tiempo.')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.show()
    
    def chart_time_1(table):
        #Crear Gráfico de líneas
        table_aux=table.sort_values(by='Time')
        fig, ax = plt.subplots(figsize=(12,6))
        print(table)
        ax.plot(table_aux['Time'], table_aux['count'], color = 'green')
        plt.xticks(rotation=90)
        plt.title('Serie de tiempo.')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.show()

    