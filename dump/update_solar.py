import pandas as pd

df1 = pd.read_csv("solar_farm.csv")

def updater():
    for day in Day:
        data ['Power'] = data['Power'] * df1['Capacity']/100
    return updater
        
       