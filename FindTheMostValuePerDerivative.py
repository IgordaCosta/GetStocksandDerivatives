import pandas
import os
from CreateCsv import CreateCsv
from datetime import datetime
from DerivadaPrediction import  DerivadaPrediction


def FindTheMostValuePerDerivative(DBcheckData, saveLocation,ValueToCheck,ColumnToCompare,numberOfMaxDerivativeDivisions,numberToSplit=None):
    
    os.chdir(os.path.dirname(__file__))
    df = pandas.read_excel(DBcheckData)

    # df.sort_index(ascending=False,inplace=True)
    
    numberOfMaxDerivativeDivisions=numberOfMaxDerivativeDivisions+2
    NumberOfMaxDivisionsChanged=False
    if numberToSplit:
        df=df.tail(numberToSplit)
        df.reset_index(drop=True)
        if numberToSplit<numberOfMaxDerivativeDivisions:
            numberOfMaxDerivativeDivisions=numberToSplit
            NumberOfMaxDivisionsChanged=True
            
    
    print(df)

  

    DerivativeOfFutureValueList=[]
    listeOfDateTimes=[]
    BuyOrSellList=[]
    StockHighList=[]
    CurrentStockList=[]
    DateOftheStockList=[]
    SubtractedValueList=[]
    GrainList=[]
    

    Stay='Stay'
    LastBuyOrSellChoice=Stay

    # print(LastBuyOrSellChoice)
 
    sizeOFDB=len(df)

    # print(sizeOFDB)

    for DerivativeNumber in range(2,numberOfMaxDerivativeDivisions):

        for i in range(sizeOFDB-DerivativeNumber):
            print(str(DerivativeNumber-1)+"/"+ str(numberOfMaxDerivativeDivisions-2),"Derivative Number")
            print(str(i)+"/"+ str(sizeOFDB-DerivativeNumber-1),"DB row")
            # print("Row in Derivative"+str(DerivativeNumber)+" is: "+ str(i))
            if DerivativeNumber==2:

               
                    # SubtractedValueList.append(0)
                # Subtraction=df[ColumnToCompare].iloc[i+1]-df[ColumnToCompare].iloc[i]

                
                if i<(sizeOFDB-DerivativeNumber-1):
                #     # print("objects")
                #     # print(df[ColumnToCompare][i],df[ColumnToCompare][i+1])
                #     # Subtraction=df[ColumnToCompare][i]-df[ColumnToCompare][i+1]
                #     Subtraction=df[ColumnToCompare].iloc[i]-df[ColumnToCompare].iloc[i+1]
                    Subtraction=df[ColumnToCompare].iloc[i+1]-df[ColumnToCompare].iloc[i]
                    SubtractedValueList.append(Subtraction)
                else:
                #     Subtraction=df[ColumnToCompare].iloc[i]-df[ColumnToCompare].iloc[i+1]
                    Subtraction=df[ColumnToCompare].iloc[i+1]-df[ColumnToCompare].iloc[i]
                    SubtractedValueList.append(Subtraction)
                    SubtractedValueList.append(0)
                # # print(SubtractedValueList)
                # # print('SubtractedValueList')
                    

            if i ==0:

                DerivativeOfFutureValueList.append([])
                listeOfDateTimes.append([])
                BuyOrSellList.append([])
                CurrentStockList.append([])
                StockHighList.append([])
                DateOftheStockList.append([])
                GrainList.append([])
                
                
                for x in range(DerivativeNumber-1):

                    DerivativeOfFutureValueList[DerivativeNumber-2].append(0)
                    listeOfDateTimes[DerivativeNumber-2].append(0)
                    BuyOrSellList[DerivativeNumber-2].append(0)
                    # print(CurrentStockList,"CurrentStockList")
                    CurrentStockList[DerivativeNumber-2].append(0)
                    # print(StockHighList,"StockHighList")
                    StockHighList[DerivativeNumber-2].append(0)
                    DateOftheStockList[DerivativeNumber-2].append(0)
                    # print(x, "X in range DerivativeNumber-1")
                    if x>0:
                        GrainList[DerivativeNumber-2].append(0)
                    

            df1=df[i:(i+DerivativeNumber)]
            DerivativeOfFutureValue, currentDateTime,DateOftheStock, BuyOrSell, StockHigh, CurrentStock=DerivadaPrediction(df=df1,ColumnToDerive=ValueToCheck,ColumnToCompare=ColumnToCompare,LastBuyOrSellChoice=LastBuyOrSellChoice,SizeOfDerivation=DerivativeNumber)
            
            DerivativeOfFutureValueList[DerivativeNumber-2].append(DerivativeOfFutureValue)
            listeOfDateTimes[DerivativeNumber-2].append(currentDateTime)
            BuyOrSellList[DerivativeNumber-2].append(BuyOrSell)
            CurrentStockList[DerivativeNumber-2].append(CurrentStock)
            StockHighList[DerivativeNumber-2].append(StockHigh)
            DateOftheStockList[DerivativeNumber-2].append(DateOftheStock)
            # SubtractedValueList.append(Subtraction)

            if i>0:
                # print(i)
                # print("I IS PRINTED ABOVE")
                # print(DerivativeOfFutureValueList[DerivativeNumber-2])
                # print(SubtractedValueList)
                # print('SubtractedValueList')
                # print(df[ColumnToCompare])
                # print("df[ColumnToCompare]")
                
                if float(DerivativeOfFutureValueList[DerivativeNumber-2][i]) > 0 and float(SubtractedValueList[i]) >0 \
                    or float(DerivativeOfFutureValueList[DerivativeNumber-2][i]) > 0 and float(SubtractedValueList[i]) <0:
                    # print(SubtractedValueList)
                    # print(i)
                    ValuetoAdd=float(SubtractedValueList[i])
                    # print(ValuetoAdd)
                    # print("Value to add obove")
                    if i==1:
                        GrainList[DerivativeNumber-2].append(ValuetoAdd)
                        # print(ValuetoAdd)
                        # print("i is = 1")
                        # print(GrainList)
                        # print("if True i==1")

                    if i<(sizeOFDB-DerivativeNumber-1):
                        # print("if True i<(sizeOFDB-DerivativeNumber-1")
                        # print(GrainList)
                        # print(i-1,"i-1")
                        # print(GrainList[DerivativeNumber-2])
                        # print(SubtractedValueList)
                        # print(i,"i")
                        OldGain=float(GrainList[DerivativeNumber-2][i-1])
                        GrainList[DerivativeNumber-2].append(OldGain+ValuetoAdd)
                        # print(GrainList)
                    else:
                        # print("if TRUE else")
                        OldGain=float(GrainList[DerivativeNumber-2][i-1])
                        GrainList[DerivativeNumber-2].append(OldGain+ValuetoAdd)
                        GrainList[DerivativeNumber-2].append(0)
                        # print("THis IS THE LAST VALUE")
                        # print(GrainList)
                else:
                    if i==1:
                        # print("else i==1")
                        GrainList[DerivativeNumber-2].append(0)
                        # print(GrainList)
                    if i<(sizeOFDB-DerivativeNumber-1):
                        # print("else i<(sizeOFDB-DerivativeNumber-1)")
                        # print(GrainList)

                        OldGain=float(GrainList[DerivativeNumber-2][i-1])

                        GrainList[DerivativeNumber-2].append(OldGain)

                        # print(GrainList)
                    else:
                        # print("else else")
                        # print(GrainList)

                        OldGain=float(GrainList[DerivativeNumber-2][i-1])

                        GrainList[DerivativeNumber-2].append(OldGain)
                        
                        GrainList[DerivativeNumber-2].append(0)
                        # print("THis IS THE LAST VALUE")
                        # print(GrainList)
                        

                    




              



            LastBuyOrSellChoice=BuyOrSell

    # print(DerivativeOfFutureValueList)

    # print(len(DerivativeOfFutureValueList),"DerivativeOfFutureValueList")
    # print(len(listeOfDateTimes),"listeOfDateTimes")
    # print(len(BuyOrSellList), "BuyOrSellList")
    # print(len(CurrentStockList), "CurrentStockList")
    
    
    # for DerivativeNumber in range(numberOfMaxDerivativeDivisions-2):
        # print(len(DerivativeOfFutureValueList[DerivativeNumber]),"DerivativeOfFutureValueList "+str(DerivativeNumber))
        # print(len(listeOfDateTimes[DerivativeNumber]),"listeOfDateTimes "+str(DerivativeNumber))
        # print(len(BuyOrSellList[DerivativeNumber]), "BuyOrSellList "+str(DerivativeNumber))
        # print(len(CurrentStockList[DerivativeNumber]), "CurrentStockList "+str(DerivativeNumber))
        # print(len(GrainList[DerivativeNumber]),"GrainList "+str(DerivativeNumber))
        # print(GrainList[DerivativeNumber])
        

    # print(len(SubtractedValueList), "SubtractedValueList")
    # print(len(GrainList),"GrainList")

    DerivativeOfFutureValuesName='Derivative Of Future Values '
    ActualDerivative="Actural Derivative"
    columns=[]
    df  = pandas.DataFrame(columns = columns)
    
    df['Stock Gain or Loss Subtraction']=SubtractedValueList
    for DerivativeNumber in range(numberOfMaxDerivativeDivisions-2):
        # print("ListItem")
        # print(DerivativeOfFutureValueList[DerivativeNumber])
        df[DerivativeOfFutureValuesName + str(DerivativeNumber)]=DerivativeOfFutureValueList[DerivativeNumber]
        df["Time and date at Function Run " + str(DerivativeNumber)]=listeOfDateTimes[DerivativeNumber]
        df["Grain "+ str(DerivativeNumber)]=GrainList[DerivativeNumber]
        df['Buy Or Sell ' + str(DerivativeNumber)]=BuyOrSellList[DerivativeNumber]
        df['Stock High ' + str(DerivativeNumber)]=StockHighList[DerivativeNumber]
        df["Current Stock " + str(DerivativeNumber)]=CurrentStockList[DerivativeNumber]
        df["Date Of the Stock"+ str(DerivativeNumber)]=DateOftheStockList[DerivativeNumber]

        

    CreateCsv(data=df,databaseName=saveLocation, alreadyDatabase=True)
    if NumberOfMaxDivisionsChanged:
        print("Amout of Derivatives changed due to database size to: " + str(numberToSplit-2))
    print("Done Max Derivatives Calculations")



MostValuePerPredictionDB='MostValuePerPredictionDB.xlsx'
databaseName='Stocks.xlsx'
ValueToCheck='2. high'
ColumnToCompare='4. close'

numberOfMaxDerivativeDivisions=15
numberToSplit=None

FindTheMostValuePerDerivative(numberToSplit=numberToSplit,DBcheckData=databaseName,saveLocation=MostValuePerPredictionDB,ValueToCheck=ValueToCheck,ColumnToCompare=ColumnToCompare,numberOfMaxDerivativeDivisions=numberOfMaxDerivativeDivisions)



####TODO Make a program that will get the derivatives for 3,4,5,6,7,8,9,10 divisions  (it must be divided by the item receiving the subtraction)
####     for each derivative division it will:
####     It will apply the Selling to the least negative derivative (closet to 0) all the way to the derivative with the largest negative value
####     It will apply the Buying to the least positive derivative (closest to 0) all the way to the derivative with the largest positive value
####     The program will then make a list of the gains for all derivative values one for the negative values and one for the positive values
####     The program will make a dictionary with the negative derivative gains as keys and the negative derivative as value
####     The program will make a dictionary with the positive derivative gains as keys and the positive derivative as value
####     Then the program must find the largest negative derivative gain and find its respective negative derivative value
####     Then the program must find the largest positive derivative gain and find its respective positive derivative value



