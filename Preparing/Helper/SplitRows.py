import math
def splitTrainColumnsAndTestColumnsRows(data,inputColumns,targetColumns):
        numberOfRows = data.shape[0]
        limit =math.floor(numberOfRows*0.8)
        Input_train =inputColumns[:limit]
        Target_train = targetColumns[:limit]
        Input_test = inputColumns[limit:]
        Target_test = targetColumns[limit:]
        return [Input_train,Target_train, Input_test, Target_test]