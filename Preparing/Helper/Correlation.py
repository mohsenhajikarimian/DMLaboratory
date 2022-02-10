import numpy as np
def dropWeakCorrelationCoulmns(Input_train, Target_train, Input_test, limit=0.5):
        for targetColumn in Target_train.columns:
                for inputColumn in Input_train.columns:
                        inputColumnCorrelationWithTargetColumn = targetColumn.corr(inputColumn)
                        if((abs(inputColumnCorrelationWithTargetColumn) < limit) | (np.isnan(inputColumnCorrelationWithTargetColumn))):
                                Input_train = Input_train.drop(inputColumn,1)
                                Input_test = Input_test.drop(inputColumn,1)
        return [Input_train, Input_test]


                 