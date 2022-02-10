from datetime import datetime
import pandas as pd
def daysBetween(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def daysBetweenColumns(d1, d2):
    #return  abs((d1- d2).dt.days)
    return  abs((pd.to_datetime(d1)- pd.to_datetime(d2)).dt.days)

    

        
