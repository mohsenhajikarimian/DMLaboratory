import pandas as pd

def readFromCSV(address, rowCounts = None):
        data = pd.read_csv(address, nrows=rowCounts)
        return data