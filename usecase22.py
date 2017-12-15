import pandas as pd 
import numpy as np
from sklearn import preprocessing 
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('usecase2/india-districts-census-2011.csv')

df1 = df.loc[df['State name'].isin(['BIHAR','TAMIL NADU'])]

tnc = df[df['State name'] == 'TAMIL NADU']
bic = df[df['State name'] == 'TAMIL NADU']
del df1['District code']
del df1['State name']

tns = tnc.shape[0]
bis = bic.shape[0]

col_name = (df1.columns).tolist()

for i in col_name[1:]:
	x = df1[i].values #returns a numpy array
	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(x)
	df1[i] = x_scaled

sim = pd.DataFrame(columns=['Dist','Sim with','Sim'])

count = 0

for i in range(0,tns+1):
	dn = df1.iloc[i][0]
	x = np.array(df1.iloc[i][1:])
	for j in range(bis,df1.shape[0]):
		sw = df1.iloc[j][0]
		y = np.array(df1.iloc[j][1:])
		si = np.dot(x,y)

		sim = sim.append({'Dist':dn, 'Sim with':sw , 'Sim':si}, ignore_index=True)


similar_districts = sim.loc[sim.Sim<1.0]

print(similar_districts)

