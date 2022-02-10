import pandas as pd
def replaceNANCellsToMeanOfColumn(data):
        numberOfRows = data.shape[0]
        numberOfCols = data.shape[1]
        meanOfColumns = data.mean(numeric_only=False)
        for i in range(numberOfRows):
                for j in range(numberOfCols):
                        if(pd.isna(data.iloc[i-1, j-1])):
                                data.iloc[i-1, j-1] = meanOfColumns[j-1]
        return data;