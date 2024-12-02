import pandas as pd
import numpy as np

class Joins:

    def __init__(self,table01,table02,SIMCARD):
        self.table01=table01
        self.table02=table02
        self.SIMCARD=SIMCARD

    def inner_join(table01,table02,SIMCARD):
        joined=table01.join(table02,how='inner',index=SIMCARD)
        print(joined)

