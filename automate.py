import pandas as pd
import numpy as np
from predict import round_data

wind_data = pd.read_csv('~/Documents/AIIP/AppDev/Summative/Uploads/wind_farm.csv', index_col=None)
solar_data = pd.read_csv('~/Documents/AIIP/AppDev/Summative/Uploads/solar_farm.csv', index_col=None)
#wind_data = wind_data.apply(pd.to_numeric, errors='coerce')
#solar_data = solar_data.apply(pd.to_numeric, errors='coerce')

# Rename the columns of both dataframe
wind_data_renamed = wind_data.rename(columns = {'Date Of Month': 'Day', 'Capacity Available as %': 'Capacity'}, inplace = False)
solar_data_renamed = solar_data.rename(columns = {'Date Of Month': 'Day', 'Capacity Available': 'Capacity'}, inplace = False)

### WIND DATA
new_wind = pd.merge(round_data, wind_data_renamed, on=['Day'])
new_wind['Power_Wind'] = new_wind['Power_Wind'] * new_wind['Capacity'] /100
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

new_solar['Power_Solar'] = new_solar['Power_Solar'] * new_solar['Capacity'] /100
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
solar_power = final_solar_data['Power_Solar']
final_wind_data["Power_Solar"] = solar_power
final_merged_data = final_wind_data
final_merged_data.to_csv('final_merged_data.csv')