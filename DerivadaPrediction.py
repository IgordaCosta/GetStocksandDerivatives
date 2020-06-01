import pandas
import os
from CreateCsv import CreateCsv
from datetime import datetime




def DerivadaPrediction(df,ColumnToDerive,ColumnToCompare,LastBuyOrSellChoice,SizeOfDerivation):
    Stay='Stay'
    Buy='Buy'
    Sell='Sell'
    StaySell='Stay Selling'
    StayBuy='Stay Buying'

    DataSortColumn='date'
    
    
    df=df.tail(SizeOfDerivation)
    df.reset_index(drop=True)
    # print(df)

    dfDate=df[DataSortColumn]

    df0=df[ColumnToCompare]

    df=df[ColumnToDerive]

    SizeOfDerivationByIndex=SizeOfDerivation-1 

    # print(SizeOfDerivationByIndex, "<<<SizeOfDerivationByIndex")

    # print(df.iloc[0],"<<<<<<df.iloc[0]" )

    # print(df.iloc[SizeOfDerivationByIndex],"<<<<<<<<df.iloc[SizeOfDerivationByIndex]")
    
   
    

    CurrentStock=df0.iloc[SizeOfDerivationByIndex]

    # OldStock=df0.iloc[SizeOfDerivation]

    # Subtraction=OldStock-CurrentStock


    StockHigh=df.iloc[SizeOfDerivationByIndex]    
    # print(df)
    # print(df.iloc[0],"df.iloc[0]")
    # print(StockHigh,"StockHigh")
    # print((StockHigh-df.iloc[0])/StockHigh,"(StockHigh-df.iloc[0])/StockHigh")

    # DerivativeOfFutureValue=(df.iloc[0]-StockHigh)/df.iloc[0]
    DerivativeOfFutureValue=(StockHigh-df.iloc[0])/StockHigh

    DateOftheStock=dfDate.iloc[SizeOfDerivationByIndex]    

    # print(DerivativeOfFutureValue)


    currentDateTime = datetime.now()

    # print(currentDateTime)

    # CheckIfBuySell=df.iloc[2]-df.iloc[1]

    BuyOrSell=''

    DerivativeOfFutureValue=float(DerivativeOfFutureValue)

    if DerivativeOfFutureValue>=0 and (LastBuyOrSellChoice==Buy or LastBuyOrSellChoice==StayBuy):
        # print(Stay)
        BuyOrSell= StayBuy
    elif DerivativeOfFutureValue<0 and (LastBuyOrSellChoice==Sell or LastBuyOrSellChoice==StaySell):
        # print(Stay)
        BuyOrSell= StaySell
    elif DerivativeOfFutureValue>=0 and (LastBuyOrSellChoice==Sell or LastBuyOrSellChoice==Stay or LastBuyOrSellChoice==StaySell):
        # print(Buy)
        BuyOrSell= Buy
    elif DerivativeOfFutureValue<0 and (LastBuyOrSellChoice==Buy or LastBuyOrSellChoice==Stay or LastBuyOrSellChoice==StayBuy):
        # print(Sell)
        BuyOrSell= Sell
    else:
        BuyOrSell='NOT EXPECTED'


    return DerivativeOfFutureValue, currentDateTime,DateOftheStock, BuyOrSell, StockHigh, CurrentStock

    # if subtraction<0:
    #     return False
    # else:
    #     return True





# SubtractOfFuturePredictionsDatabaseName='SubtractOfFuturePredictions.xlsx'
# FurePredictionsDatabaseName='FuturePredictions.xlsx'
# databaseName='Stocks.xlsx'
# ValueToCheck='2. high'
# ColumnToCompare='4. close'

# numberToSplit=50

# os.chdir(os.path.dirname(__file__))
# df = pandas.read_excel(databaseName)

# # df=df.head(200)

# print(df)

# # df1=df[10:20]

# numberOfRows=3

# # print(df1)
# listOfSubtractedFutureValues=[]
# listeOfDateTimes=[]
# BuyOrSellList=[]
# CurrentStockList=[]
# # for x in range(len(df)-numberOfRows):
# Stay='Stay'
# LastBuyOrSellChoice=Stay

# print(LastBuyOrSellChoice)

# # for x in range(2):
# #     print(LastBuyOrSellChoice)
# #     df1=df[x:(x+numberOfRows)]
# #     subtraction, currentDateTime, BuyOrSell=DerivadaPrediction(df=df1,ColumnToDerive=ValueToCheck,LastBuyOrSellChoice=LastBuyOrSellChoice)
# #     print(subtraction, currentDateTime, BuyOrSell)
# #     print("subtraction, currentDateTime, BuyOrSell")
# #     print(BuyOrSell)
# #     print("BuyOrSell")

# for x in range(len(df)-numberOfRows):
#     print("X chosen: ",x)
#     df1=df[x:(x+numberOfRows)]
#     # print(df1)
#     subtraction, currentDateTime, BuyOrSell, CurrentStock=DerivadaPrediction(df=df1,ColumnToDerive=ValueToCheck,ColumnToCompare=ColumnToCompare,LastBuyOrSellChoice=LastBuyOrSellChoice)
#     listOfSubtractedFutureValues.append(subtraction)
#     listeOfDateTimes.append(currentDateTime)
#     BuyOrSellList.append(BuyOrSell)
#     CurrentStockList.append(CurrentStock)
#     LastBuyOrSellChoice=BuyOrSell

# print(listOfSubtractedFutureValues)

# columns=[]
# df  = pandas.DataFrame(columns = columns)
# df['Subtract Of Future Values']=listOfSubtractedFutureValues
# df["Time and date at Function Run"]=listeOfDateTimes
# df['Buy Or Sell']=BuyOrSellList
# df["Current Stock"]=CurrentStockList

# CreateCsv(data=df,databaseName=SubtractOfFuturePredictionsDatabaseName, alreadyDatabase=True)


####TODO Make a program that will get the derivatives for 3,4,5,6,7,8,9,10 divisions  (it must be divided by the item receiving the subtraction)
####     for each derivative division it will:
####     It will apply the Selling to the least negative derivative (closet to 0) all the way to the derivative with the largest negative value
####     It will apply the Buying to the least positive derivative (closest to 0) all the way to the derivative with the largest positive value
####     The program will then make a list of the gains for all derivative values one for the negative values and one for the positive values
####     The program will make a dictionary with the negative derivative gains as keys and the negative derivative as value
####     The program will make a dictionary with the positive derivative gains as keys and the positive derivative as value
####     Then the program must find the largest negative derivative gain and find its respective negative derivative value
####     Then the program must find the largest positive derivative gain and find its respective positive derivative value



