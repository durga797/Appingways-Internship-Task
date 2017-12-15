import pandas as pd 
import numpy as np 
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib


df = pd.read_csv('usecase2/india-districts-census-2011.csv')

df2 = df[['State name','Agricultural_Workers''Households_with_Telephone_Mobile_Phone_Mobile_only']].copy()
df2.columns = ['STATE' ,'AGRW','TMO']

df1 = df2.groupby('STATE').sum()

arr = np.array(df1.TMO)
arr1 = np.array(df1.AGRW)

arr1[arr1 == 0] = 1

rate = np.true_divide(arr,arr1)

#plt.plot(df1.index.values,rate)

#matplotlib.axes.Axes.tick_params(axis='both',length=4.0)
x = [i for i in range(0,df1.shape[0])]
xTicks = df1.index.values.tolist()
y = rate
pl.xticks(x, xTicks)
axes = plt.gca()
axes.set_ylim([0,10])
pl.xticks(range(df1.shape[0]), xTicks, rotation=90) #writes strings with 45 degree angle
pl.plot(x,y,'*')
pl.ylabel('Penetration Rate')
pl.xlabel('State Name')
pl.show()

pl.savefig('plot.png')