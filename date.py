import pandas as pd

class Date():
    def __init__(self,table02):
        self.table02=table02
    
    def order_date(table02):
        path=table02
        df=pd.read_csv(path)
        df_ymd=pd.DataFrame()
        df_ymd_filter=pd.DataFrame()
        df_ymd_filter_dt=pd.DataFrame()
        #df['Primeras_3_letras'] = df['Nombre'].apply(lambda x: x[:3])
        #df_ymd['Time']=df['Time'].apply(lambda x:x[0:10])        
        #df_ymd_filter['Time']=pd.to_datetime(df_ymd['Time'].strftime("%Y-%m-%d"))
        #print(df_ymd)        
        df_filter=df[['Time']]
        #df_ymd_filter=df_ymd[['Time']]        
        print("Trabajando...")
        df_filter['Time']=pd.to_datetime(df['Time'])
        #df_ymd['Time']=(df_filter['Time']).apply(lambda x:x[0:9])
        #df_ymd_filter['Time']=pd.to_datetime(df_ymd['Time'])
        #print(df_ymd.head(5))        
        #print(df_ymd_filter.info())
        df_filter.sort_values(by='Time', ascending=True)
        df_ymd_filter['Time']=df_filter['Time'].dt.strftime('%Y-%m-%d')
        df_ymd_filter_dt['Time']=pd.to_datetime(df_ymd_filter['Time'])        
        print(df_ymd_filter_dt)
        #df_ymd_filter.sort_values(by='Time', ascending=True)
        #print(df_filter)
        #df_filter_date=df_filter[(df_filter['Date'].dt.month>8)&(df_filter['Date'].dt.day>26)]
        #print(df_filter_date)
        #print("\n")        
        option=input("\nDesea crear un reporte S/N:\n")
        if option=='S':
            df_filter.to_csv('Date_ordered.csv')
            df_ymd_filter_dt.to_csv('Date_ordered_ymd.csv')