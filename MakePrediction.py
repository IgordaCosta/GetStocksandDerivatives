import pandas
import numpy as np  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

from DerivadaPrediction import DerivadaPrediction

from CreateCsv import CreateCsv

databaseName='Predictions.xlsx'

FurePredictionsDatabaseName='FuturePredictions.xlsx'

SubtractOfFuturePredictionsDatabaseName='SubtractOfFuturePredictions.xlsx'

def MakeLinearRegression(df,xValues,yValues):
    os.chdir(os.path.dirname(__file__))

    df.reset_index(level=0, inplace=True)

    #X = df[xValues].values.reshape(-1,1)
    X = df.index.values.reshape(-1,1)
    y = df[yValues].values.reshape(-1,1)

    print(X)

    NumberOfCharacters=len(X)
    print(NumberOfCharacters)

    TwentyPercertOfCharacters=int(NumberOfCharacters/5)    
    print(TwentyPercertOfCharacters)

    FuturePredictionsRange=np.array(range(NumberOfCharacters+TwentyPercertOfCharacters)).reshape(-1,1)

    print(FuturePredictionsRange)


    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    X_train= X[slice(NumberOfCharacters-TwentyPercertOfCharacters)]

    X_test= X[slice(NumberOfCharacters-TwentyPercertOfCharacters, NumberOfCharacters)]


    y_train= y[slice(NumberOfCharacters-TwentyPercertOfCharacters)]

    y_test= y[slice(NumberOfCharacters-TwentyPercertOfCharacters, NumberOfCharacters)]
    

    print(X_test)

    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    xcolumnName="Value Referenced"

    df = pandas.DataFrame({xcolumnName: X_test.flatten() ,'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

    pandas.DataFrame.sort_values(df, by=xcolumnName, inplace=True)

    print(df)

    CreateCsv(data=df,databaseName=databaseName, alreadyDatabase=True)

    FuturePredictions = regressor.predict(FuturePredictionsRange)

    df = pandas.DataFrame({'Predicted': FuturePredictions.flatten()})

    print(df)

    CreateCsv(data=df,databaseName=FurePredictionsDatabaseName, alreadyDatabase=True)

    print("done Predictions")


def MakeLinearRegressionFuture(df,yValues):
    os.chdir(os.path.dirname(__file__))

    df.reset_index(level=0, inplace=True)

    #X = df[xValues].values.reshape(-1,1)
    X = df.index.values.reshape(-1,1)
    y = df[yValues].values.reshape(-1,1)

    # print(X)

    NumberOfCharacters=len(X)
    # print(NumberOfCharacters)

    TwentyPercertOfCharacters=2   
    # print(TwentyPercertOfCharacters)

    # FuturePredictionsRange=np.array(range(NumberOfCharacters+TwentyPercertOfCharacters)).reshape(-1,1)
    FuturePredictionsRange=np.array(range(NumberOfCharacters,NumberOfCharacters+TwentyPercertOfCharacters)).reshape(-1,1)

    # print(FuturePredictionsRange)


    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    X_train= X[slice(NumberOfCharacters-TwentyPercertOfCharacters)]

    X_test= X[slice(NumberOfCharacters-TwentyPercertOfCharacters, NumberOfCharacters)]


    y_train= y[slice(NumberOfCharacters-TwentyPercertOfCharacters)]

    y_test= y[slice(NumberOfCharacters-TwentyPercertOfCharacters, NumberOfCharacters)]
    

    # print(X_test)

    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)

    # y_pred = regressor.predict(X_test)

    # xcolumnName="Value Referenced"

    # df = pandas.DataFrame({xcolumnName: X_test.flatten() ,'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

    # pandas.DataFrame.sort_values(df, by=xcolumnName, inplace=True)

    # print(df)

    # CreateCsv(data=df,databaseName=databaseName, alreadyDatabase=True)

    FuturePredictions = regressor.predict(FuturePredictionsRange)

    print(FuturePredictions)

    SubtractionFutureValues=FuturePredictions[1][0]-FuturePredictions[0][0]

    print(SubtractionFutureValues)

    return SubtractionFutureValues

    # df = pandas.DataFrame({'Predicted': FuturePredictions.flatten()})

    # print(df)

    # CreateCsv(data=df,databaseName=FurePredictionsDatabaseName, alreadyDatabase=True)

    print("done Predictions")


databaseName='Stocks.xlsx'
closeValue='4. close'

numberToSplit=50

os.chdir(os.path.dirname(__file__))
df = pandas.read_csv(databaseName)

df=df.head(200)

print(df)

# df1=df[10:20]

numberOfRows=50

# print(df1)
listOfSubtractedFutureValues=[]
# for x in range(len(df)-numberOfRows):
for x in range(numberOfRows,len(df)-numberOfRows):
    print("X chosen: ",x)
    df1=df[x:(x+1+numberOfRows)]
    # print(df1)
    SubtractionFutureValues=MakeLinearRegressionFuture(df=df1,yValues=closeValue)
    listOfSubtractedFutureValues.append(SubtractionFutureValues)

print(listOfSubtractedFutureValues)

columns=[]
df  = pandas.DataFrame(columns = columns)
df['SubtractOfFutureValues']=listOfSubtractedFutureValues

CreateCsv(data=df,databaseName=SubtractOfFuturePredictionsDatabaseName, alreadyDatabase=True)







# df_split = np.array_split(df, numberToSplit)

# print(df_split[0])
# print(df_split[1])
# print(df_split[2])
# print(df_split[3])




# df=df_split[2]

# print(df)

# print(df[closeValue])

# MakeLinearRegressionFuture(df=df,yValues=closeValue)




# # df = pandas.DataFrame(np.random.randint(0,122,size=(122, 4)), columns=list('ABCD'))
# columns=[]
# df  = pandas.DataFrame(columns = columns)

# rangeOfValues=120

# column1Name='values1'
# Column2Name='values3'

# df['values1']=range(rangeOfValues)
# df['values3']=[x*3 for x in range(rangeOfValues)]

# print(df.index.values)

# MakeLinearRegression(df,'values1','values3')

