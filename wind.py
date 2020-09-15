# Import required libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn import linear_model # for linear regression modeling
from sklearn import preprocessing # for preprocessing like imputting missing values

# Import data
data = pd.read_csv("wind_generation_data.csv")

# View data and fill null values
print(data.head())
print(data.dtypes)
print(data.shape)
print(data.isnull().sum())

# Refine data for model
X = data.drop(['Power Output'], axis=1).values # X are the input (or independent) variables
y = data['Power Output'].values # Y is output (or dependent) variable

# Create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#Fit data to mol
lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

# save the model to disk
filename = 'wind_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)