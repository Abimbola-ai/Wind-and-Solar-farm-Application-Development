import pandas as pd
import numpy as np
import pickle
from sklearn import linear_model

new_data = pd.read_csv('merged.csv', index_col=[0])

#print(new_data.dtypes)
#print(new_data)
solar_feat = new_data.drop(['prediction_num','datetime','windspeed', 'Direction', 'Day', 'Month'], axis=1)
wind_feat = new_data.drop(['prediction_num','datetime','Temp_Hi', 'Temp_Low', 'Cloud', 'Solar', 'Rainfall','Day', 'Month'], axis=1)
#print(solar_feat)
#print(wind_feat)

X_solar = solar_feat.values
X_wind = wind_feat.values

#Load solar model from disk
solar_model = pickle.load(open('solar_model.pkl', 'rb'))
Power_Solar = solar_model.predict(X_solar)
#print(Power_Solar)

#Load wind model from disk
wind_model = pickle.load(open('wind_model.pkl', 'rb'))
Power_Wind = wind_model.predict(X_wind)
#print(Power_Wind)

# Output data for solar

new_data['Power_Solar'] = Power_Solar
new_data['Power_Wind'] = Power_Wind
new_data = new_data.drop(['prediction_num','datetime'], axis=1)
round_data = new_data.round(2)
round_data.to_csv("new_data.csv")