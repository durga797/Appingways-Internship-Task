import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import geopandas as gpd


df = pd.read_csv('usecase2/india-districts-census-2011.csv')

new = df[['State name', 'Population','Literate']].copy()



df1 = new.groupby('State name').sum()

popul = np.array(df1.Population)
liter = np.array(df1.Literate)

lit_rate = np.true_divide(liter,popul)

state_name = (df1.index.get_values()).tolist()

state_name.append('Telengana')

#state_lit = pd.DataFrame({'State':state_name,'Literacy':lit_rate})

data = gpd.read_file('usecase2/Boundaries/India-States.shp')
lis =  [data.loc[data.ST_NM.isin(['Telangana','Andhra Pradesh'])].geometry ] 

print lis

# data.plot()

# plt.show()