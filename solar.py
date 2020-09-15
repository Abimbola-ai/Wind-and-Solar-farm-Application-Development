import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model # for linear regression modeling
from sklearn import preprocessing # for preprocessing like imputting missing values
import pickle



data = pd.read_csv("solar_generation_data.csv")
data['Temp Hi'] = data['Temp Hi'].replace('\u00b0','', regex=True).astype(float)
data['Temp Low'] = data['Temp Low'].replace('\u00b0','', regex=True).astype(float)

print(data.head())
print(data.dtypes)
print(data.shape)

data_fill = data.fillna(0)
print(data_fill.isnull().sum())
data_model = data_fill[['Temp Hi', 'Temp Low', 'Solar', 'Cloud Cover Percentage', 'Rainfall in mm', 'Power Generated in MW']]

X = data_model.drop(['Power Generated in MW'], axis=1).values # X are the input (or independent) variables
y = data_model['Power Generated in MW'].values # Y is output (or dependent)

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

# save the model to disk
filename = 'solar_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)