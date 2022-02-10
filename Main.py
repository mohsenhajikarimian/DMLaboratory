# %%
import math
import numpy as np
from sklearn.linear_model import LogisticRegression
from xgboost import XGBRegressor
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
from sklearn import utils
from Preparing.DataCollection import collectData
from Config import setConfig
from Preprocessing.Normalize.MinMax import normalize
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics import mean_squared_error
from sklearn import svm
from sklearn.metrics import mean_absolute_error
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn import tree
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from datetime import datetime
import seaborn as sns
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier


def calculateErrors(Target_test_normal,Target_predicted_Normal):
        error_MAE = round(mean_absolute_error(Target_test_normal, Target_predicted_Normal),3)
        error_MSE = round(mean_squared_error(Target_test_normal, Target_predicted_Normal, squared=True),3)
        error_RMSE = round(mean_squared_error(Target_test_normal,Target_predicted_Normal, squared=False),3)
        return [error_MAE, error_MSE,error_RMSE]

def printErrors(modelName ,columnName, error_MAE, error_MSE, error_RMSE):
        print(modelName + " for " + columnName + " => MAE: "+ str(error_MAE) + " MSE: "+ str(error_MSE) + " RMSE: " + str(error_RMSE) )

def predictModel(model, Input_train_normal, Target_train_normal):
        wrapper = MultiOutputRegressor(model)
        wrapper.fit(Input_train_normal, Target_train_normal)
        Target_predicted_Normal = wrapper.predict(Input_test_normal)       
        return Target_predicted_Normal

def convertListOfArraysToDataframe(Target_predicted_Normal, columns):
        Target_predicted_Normal = pd.DataFrame(Target_predicted_Normal)
        Target_predicted_Normal.columns =columns
        return Target_predicted_Normal

headers = []
data = []
# setConfig()

[Input_train,Target_train, Input_test, Target_test] =  collectData('./Dataset/PatientInfo.csv')

Input_train_normal = normalize(Input_train)
Input_test_normal = normalize(Input_test)
Target_train_normal = normalize(Target_train)
Target_test_normal = normalize(Target_test)


#LinearRegression
Target_predicted_Normal = predictModel(linear_model.LinearRegression(),Input_train_normal,Target_train_normal)
[error_MAE, error_MSE,error_RMSE] = calculateErrors(Target_test_normal, Target_predicted_Normal)
printErrors('LinearRegression','state',error_MAE, error_MSE,error_RMSE)

#SVM/SVR
Target_predicted_Normal = predictModel(SVR(kernel='linear'),Input_train_normal,Target_train_normal)
[error_MAE, error_MSE,error_RMSE] = calculateErrors(Target_test_normal, Target_predicted_Normal)
printErrors('SVM/SVR','state',error_MAE, error_MSE,error_RMSE)

#DecisionTreeRegressor
Target_predicted_Normal = predictModel( tree.DecisionTreeRegressor(),Input_train_normal,Target_train_normal)
[error_MAE, error_MSE,error_RMSE] = calculateErrors(Target_test_normal, Target_predicted_Normal)
printErrors('DecisionTreeRegressor','state',error_MAE, error_MSE,error_RMSE)

#KNeighborsRegressor
Target_predicted_Normal = predictModel( KNeighborsRegressor(),Input_train_normal,Target_train_normal)
[error_MAE, error_MSE,error_RMSE] = calculateErrors(Target_test_normal, Target_predicted_Normal)
printErrors('KNeighborsRegressor','state',error_MAE, error_MSE,error_RMSE)

#XGBRegressor
Target_predicted_Normal = predictModel( XGBRegressor(),Input_train_normal,Target_train_normal)
[error_MAE, error_MSE,error_RMSE] = calculateErrors(Target_test_normal, Target_predicted_Normal)
printErrors('XGBRegressor','state',error_MAE, error_MSE,error_RMSE)