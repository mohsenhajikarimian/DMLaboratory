import pandas as pd

def normalize(data):
#   numericTypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
#   print(type(data))
#   data = data.select_dtypes(include=numericTypes)

  numberOfRows = data.shape[0]
  numberOfCols = data.shape[1]
  maxOfColumns = data.max(numeric_only=False)
  minOfColumns = data.min(numeric_only=False)
  for i in range(numberOfRows):
    for j in range(numberOfCols):
        if(maxOfColumns[j-1] - minOfColumns[j-1] != 0):
            data.iloc[i-1, j-1] = (data.iloc[i-1, j-1] - minOfColumns[j-1])/(maxOfColumns[j-1]- minOfColumns[j-1])
        else:
            data.iloc[i-1, j-1] = 0

  meanOfNormalColumns = data.mean(numeric_only=False)
  for i in range(numberOfRows):
    for j in range(numberOfCols):
        if(pd.isna(data.iloc[i-1, j-1])):
            data.iloc[i-1, j-1] = meanOfNormalColumns[j-1]
  return data