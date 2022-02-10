def dropColumnsWhichHasNANValues(data) #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
        data.dropna(how='all', axis='columns', inplace=True)#Note => axis=1 is equal to axis='columns'.
        return data