
import pandas
from alpha_vantage.timeseries import TimeSeries
import sys
import os
import random
import matplotlib.pyplot as plt
import time

from PlotGraph import plotGraph, multiGraphPlot
from CreateCsv import CreateCsv
from FunctionCheckStock import CheckStock
from GetRamdomKeyFromFile import GetRandomKey
# from MakePrediction import MakeLinearRegression




# OutOfUsStock="NSE:"

ticker='SNDL'
# ticker=OutOfUsStock+ticker
databaseName='Stocks.xlsx'
# numberOfGraphs=20





def checkStock(ticker=ticker,databaseName=databaseName):
    os.chdir(os.path.dirname(__file__))
    returnedValue=None
    DoneGettingValue=False
    DataSortColumn='date'
    ColumnToCompare='4. close'

    while DoneGettingValue==False:
        Keys=GetRandomKey(filename='keys.txt')
        print(Keys)

        returnedValue, DoneGettingValue=CheckStock(ticker=ticker,keys=Keys)

        if DoneGettingValue==False:
            print(ticker)
            print('Connection Error! Trying Again...')
            time.sleep(5)

    print("Value returned Successfully")
    print(returnedValue)

    df=CreateCsv(data=returnedValue,databaseName=databaseName,DataSortColumn=DataSortColumn)

    multiGraphPlot(df,numberOfGraphs=30,xValues=DataSortColumn,yValues=ColumnToCompare,graphType="line")
    print("Database updated!")
    print(df)
    print("Database Above!")
    
    
    

checkStock(ticker=ticker,databaseName=databaseName)

#plotGraph(df=df,xValues='date',yValues='4. close')

#multiGraphPlot(df=df,numberOfGraphs=numberOfGraphs,xValues='date',yValues='4. close')

# x,y=df.shape

# MakeLinearRegression(df=df,xValues='date',yValues='4. close')

# print("done")

