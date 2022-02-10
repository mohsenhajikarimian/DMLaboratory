def dropRowsIfSpecificCellIsSomething(data,column,value):
        for index, row in data.iterrows():
                if(row[column]==value):
                        data.drop(index, inplace=True)
        return data

def dropRowsWhichHasNANValue(data) #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
        data.dropna(how='any', axis='index', inplace=True)#Note => axis=0 is equal to axis='index' 
        return data
