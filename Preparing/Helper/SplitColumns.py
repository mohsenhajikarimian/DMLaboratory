import pandas as pd

def splitDateColumnsToYearMonthDayColumns(data,columns):
        for column in columns:
                data[column+'_year']= pd.to_datetime(data[column],format='%m/%d/%Y').dt.year
                data[column+'_month']= pd.to_datetime(data[column],format='%m/%d/%Y').dt.month
                data[column+'_day']= pd.to_datetime(data[column],format='%m/%d/%Y').dt.day
        data = data.drop(columns,1)
        return data;

def splitAsOneHotEncoding(data,columns):
        for column in columns:
                data = pd.get_dummies(data, columns=[column])
        return data;

def splitInputAndTargetColumn(data,column):
        targetColumn =  pd.DataFrame(data[column], columns=[column])
        inputColumns = data.drop(column,1)
        return [inputColumns,targetColumn]

