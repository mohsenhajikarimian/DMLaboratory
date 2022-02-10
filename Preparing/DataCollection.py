import warnings
import matplotlib as mpl
warnings.simplefilter(action='ignore', category=FutureWarning)
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR
import seaborn as sns
from Preparing.Helper.ParseColumns import parsePriceColumnsToNumericColumns
from Preparing.Helper.ParseColumns import parseDecateColumnsToNumericColumns
from Preparing.Helper.SplitColumns import splitDateColumnsToYearMonthDayColumns
from Preparing.Helper.SplitColumns import splitAsOneHotEncoding
from Preparing.Helper.SplitColumns import splitInputAndTargetColumn
from Preparing.Helper.ReplaceNANCells import  replaceNANCellsToMeanOfColumn
from Preparing.Helper.SplitRows import splitTrainColumnsAndTestColumnsRows
from Preparing.Helper.IO import  readFromCSV
from Preparing.Helper.Correlation import dropWeakCorrelationCoulmns
from Preparing.Helper.Date import daysBetweenColumns
from Preparing.Helper.Sort import sortByColumns
from Preparing.Helper.dropRows import dropRowsIfSpecificCellIsSomething
from Preparing.Helper.ParseColumns import parseColumnToBinary

def collectData(address, rowCounts=None):
        data = readFromCSV(address, rowCounts)
        # print(data.head())
        ## PRINT COLUMN TYPES
        ##https://dev.to/chanduthedev/how-to-display-all-rows-from-data-frame-using-pandas-dha
        # pd.set_option('display.max_rows', data.shape[0]+1)
        ##https://pbpython.com/categorical-encoding.html
        # print(data.dtypes)
        data = data[['sex','age','infection_case','confirmed_date','released_date','state']]
        data['No_day'] = daysBetweenColumns(data['released_date'], data['confirmed_date'])
        data=data.drop('released_date',1)
        data=data.drop('confirmed_date',1)
        data = parseDecateColumnsToNumericColumns(data,columns = ['age'])
        data = dropRowsIfSpecificCellIsSomething(data,'state','isolated')
        data = splitAsOneHotEncoding(data,columns = ['sex','infection_case'])
        data = parseColumnToBinary(data,'state',zero='deceased',one='released')
        data = replaceNANCellsToMeanOfColumn(data)
        [inputColumns,targetColumn] = splitInputAndTargetColumn(data,'state')
        # print(inputColumns)
        # print(targetColumn)
        [Input_train,Target_train, Input_test, Target_test] = splitTrainColumnsAndTestColumnsRows(data, inputColumns,targetColumn)
        # [Input_train,Input_test] = dropWeakCorrelationCoulmns(Input_train, Target_train, Input_test, limit=0.5)
        # displayCorrelationDiagram(Input_train, Target_train)
        return [Input_train,Target_train, Input_test, Target_test]