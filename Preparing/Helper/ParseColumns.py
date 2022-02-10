import pandas as pd

def parsePriceColumnsToNumericColumns(data,columns):
        for column in columns:
                data[column] = pd.to_numeric(data[column].str.replace('$',''))
        return data

def parseDecateColumnsToNumericColumns(data,columns):
        for column in columns:
                data[column] = pd.to_numeric(data[column].str.replace('s',''))
        return data

def parseColumnToBinary(data,column,one,zero):
        
        for index, row in data.iterrows():
                if(row[column]==one):
                        data.loc[index,column]=1
                if(row[column]==zero):
                        data.loc[index,column]=0
        return data
