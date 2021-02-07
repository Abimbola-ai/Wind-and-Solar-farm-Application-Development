#Import Libraries
import pandas as pd
import numpy as np
from predict import round_data
from twilio.rest import Client
import os
from datetime import datetime

#Read in uploaded maintenance data, use your computer directory below
wind_data = pd.read_csv('~/Documents/Learning/Wind-and-Solar-farm-Application-Development/Uploads/wind_farm.csv', index_col=None)
solar_data = pd.read_csv('~/Documents/Learning/Wind-and-Solar-farm-Application-Development/Uploads/solar_farm.csv', index_col=None)


# Rename the columns of both dataframe
wind_data_renamed = wind_data.rename(columns = {'Date Of Month': 'Day', 'Capacity Available as %': 'Capacity'}, inplace = False)
solar_data_renamed = solar_data.rename(columns = {'Date Of Month': 'Day', 'Capacity Available': 'Capacity'}, inplace = False)

#print(wind_data_renamed)
### WIND DATA
new_wind = pd.merge(round_data, wind_data_renamed, on=['Day'])
new_wind['Predicted_WindFarm_Output(MW)'] = new_wind['Predicted_WindFarm_Output(MW)'] * new_wind['Capacity'] /100
final_wind = pd.merge(round_data, new_wind, how='outer', on='Day', suffixes=('_',''))
final_wind_data = final_wind.drop(['Capacity'], axis=1)
new_cols = final_wind_data.columns[final_wind_data.columns.str.endswith('_')]

#remove last char from column names
orig_cols = new_cols.str[:-1]
#dictionary for rename
d = dict(zip(new_cols, orig_cols))

#filter columns and replace NaNs by new appended columns
final_wind_data[orig_cols] = final_wind_data[orig_cols].combine_first(final_wind_data[new_cols].rename(columns=d))
#remove appended columns 
final_wind_data = final_wind_data.drop(new_cols, axis=1)
#final_wind_data.to_csv("corrected_wind_data.csv")

### SOLAR DATA
new_solar = pd.merge(round_data, solar_data_renamed, on=['Day'])

new_solar['Predicted_SolarFarm_Output(MW)'] = new_solar['Predicted_SolarFarm_Output(MW)'] * new_solar['Capacity'] /100
final_solar = pd.merge(round_data, new_solar, how='outer', on='Day', suffixes=('_',''))
final_solar_data = final_solar.drop(['Capacity'], axis=1)
new_cols_ = final_solar_data.columns[final_solar_data.columns.str.endswith('_')]

#remove last char from column names
orig_cols_ = new_cols_.str[:-1]
#dictionary for rename
e = dict(zip(new_cols_, orig_cols_))

#filter columns and replace NaNs by new appended columns
final_solar_data[orig_cols_] = final_solar_data[orig_cols].combine_first(final_solar_data[new_cols_].rename(columns=e))
#remove appended columns 
final_solar_data = final_solar_data.drop(new_cols, axis=1)
#final_solar_data.to_csv("corrected_solar_data.csv")

### MERGE BOTH TO ONE DF
solar_power = final_solar_data['Predicted_SolarFarm_Output(MW)']
final_wind_data["Predicted_SolarFarm_Output(MW)"] = solar_power
final_merged_data = final_wind_data
final_merged_data = final_merged_data.rename(columns = {"Predicted_SolarFarm_Output(MW)":"SolarFarm_Output(MW)",
"Predicted_WindFarm_Output(MW)":"WindFarm_Output(MW)"})
#final_merged_data.to_csv('final_merged_data.csv')
#print(final_merged_data)

final_merged_data['Total_MW'] = (final_merged_data['SolarFarm_Output(MW)'] + final_merged_data["WindFarm_Output(MW)"]).round(2)
#print(final_merged_data)
#final_merged_data.to_csv('final_merged_data.csv')
less_data = final_merged_data[(final_merged_data.Total_MW <= 4.0)]

account_sid = "xxxx" #input twilio account SID
auth_token = "yyyy" #input twilio auth token

client = Client(account_sid, auth_token)

def send_message2(message2):
    message2 = client.messages.create(
        from_='whatsapp:+14155238886',  #use twilio number
        body=message2, 
        to='whatsapp:+2348106061236') #use your number
    return message2

current_timestamp = str(datetime.now())
messages2 = f"Report for Output less than 4MW @ {current_timestamp}" 

rowz = zip(less_data['Day'].tolist(), less_data['Total_MW'].tolist())
for row in rowz:
    message_partition2 = f"""
    [{row[0]}]

    Total Power Generated in MW = {str(row[1])}"""
    messages2 = messages2 + message_partition2

#print(messages2)
send_message2(messages2)