from alpha_vantage.timeseries import TimeSeries
import sys
import os
import random
# from GetRamdomKeyFromFile import GetRandomKey

def CheckStock(keys,ticker=None):
    if ticker==None:
        data=None
        print("choose a ticker")
        
    else:
        try:
            time=TimeSeries(key=keys, output_format='pandas')
            dataFirst= time.get_intraday(symbol=ticker, interval= '1min', outputsize='full')
            data=dataFirst[0]
            print(data)
            Done=True
        except Exception as e:
            print(e)
            data=None
            Done=False

    return data, Done

# Keys=GetRandomKey(filename='keys.txt',randomKey='no')

# print(Keys)


# ticker='AAPL'

# CheckStock(keys=Keys,ticker=ticker)

