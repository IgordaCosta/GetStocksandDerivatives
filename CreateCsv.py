import pandas
import os

def CreateCsv(data,databaseName,DataSortColumn=None,alreadyDatabase=False):
    if alreadyDatabase==False:
        df = pandas.DataFrame(data)
    else:
        df=data

    if DataSortColumn:
        df=df.sort_index(ascending=True)
        print("DATAFRAME ORDER REVERSED!")

    df.to_excel(databaseName)

    return df


# os.chdir(os.path.dirname(__file__))
# SubtractOfFuturePredictionsDatabaseName='SubtractOfFuturePredictions.xlsx'


# columns=[]
# df  = pandas.DataFrame(columns = columns)

# rangeOfValues=120

# column1Name='values1'
# Column2Name='values3'

# df['values1']=range(rangeOfValues)
# df['values3']=[x*3 for x in range(rangeOfValues)]

# CreateCsv(df,databaseName=SubtractOfFuturePredictionsDatabaseName,alreadyDatabase=True)

# print("done")

