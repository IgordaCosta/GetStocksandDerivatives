import pandas
import matplotlib.pyplot as plt
import numpy as np
import os




def plotGraph(df,xValues,yValues,graphType="line"):
    ax = plt.gca()

    df.reset_index(level=0, inplace=True)

    df.plot(kind=graphType,x=xValues,y=yValues,ax=ax)


    plt.show()

def multiGraphPlot(df,numberOfGraphs,xValues,yValues,graphType="line"):
    # ax = plt.gca()

    df.reset_index(level=0, inplace=True)

    x,y=df.shape

    print(x, " xvalues")   

    stepDivide= x // numberOfGraphs

    for step in range(numberOfGraphs):
        
        stopCut=(step+1)*stepDivide
        print(stopCut)
        if step==0:
            print("step 0: ",step)
            df1 = df.iloc[:stopCut, :]
            # print(df1)
            # df1.plot(kind=graphType,x=xValues,y=yValues,ax=ax)
            # plt.show()
        elif step==numberOfGraphs-1:
            StartCut=(step)*stepDivide
            print("step if number of graphs: ",step)
            df1 = df.iloc[StartCut:x, :]
            # print(df1)
            # df1.plot(kind=graphType,x=xValues,y=yValues,ax=ax)
            # plt.show()
        else:
            print("step else: ",step)
            StartCut=(step)*stepDivide
            df1 = df.iloc[StartCut:stopCut, :]
            # print(df1)
            # df1.plot(kind=graphType,x=xValues,y=yValues,ax=ax)
            # plt.show()

        

        
        #plt.rc('figure', figsize=(ImageSize, ImageSize))
        fig = plt.figure() 
        ax = fig.add_subplot(1, 1, 1)
        plt.rcParams.update({'figure.autolayout': True})
        print('passed initial 1')
                
        # for Names in range(NumberChoicesCheck):
                    
        #     ColorUsed=str(self.HexRGBColors(R=RGBChoices[Names][0],G=RGBChoices[Names][1],B=RGBChoices[Names][2]))
        #     print(ColorUsed)
                
        ax.plot(df1[xValues],df1[yValues] , color= 'blue',  marker= 'o', linestyle ='-', label= xValues)
                
        ax.legend(loc='best')
        labels = ax.get_xticklabels()
        print('ok6')
        plt.setp(labels, rotation=45, horizontalalignment='right')

        ax.set(xlabel=xValues, ylabel= yValues,
                title=yValues+" x "+ xValues +' (Grafico) '+str(step))
        print('ok7')
        ax.grid(b= True, color='grey', linestyle='--', linewidth=0.5)
            
        filename=yValues+' x '+ xValues + ' Grafico '+str(step)+'.png'
                
        plt.savefig(filename, dpi=400, bbox_inches='tight')

        os.startfile(filename)


    print("end stopped cut",stopCut)

    # print(df)

    # df.plot(kind=graphType,x=xValues,y=yValues,ax=ax)


    # plt.show()


#df = pandas.DataFrame(np.random.randint(0,122,size=(122, 4)), columns=list('ABCD'))
# columns=[]
# df  = pandas.DataFrame(columns = columns)

# rangeOfValues=120

# column1Name='values1'
# Column2Name='values3'

# df['values1']=range(rangeOfValues)
# df['values3']=[x*3 for x in range(rangeOfValues)]

# print(df)

# multiGraphPlot(df=df,numberOfGraphs=3,xValues="values1",yValues='values3')

### TODO find why it is only printing one graph and not multiple graphs
### TODO add graphing system from NH Descontos program