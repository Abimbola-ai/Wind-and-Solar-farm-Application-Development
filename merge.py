import csv
from collections import OrderedDict
import os
import pandas as pd
from weather_solar import *
from weather_wind import *


### MERGE ALL ACQUIRED DATA TO ONE DATAFRAME
weather_solar['windspeed'] = weather_wind['windspeed']
weather_solar['Direction'] = weather_wind['Direction']
#weather_solar.to_csv('new_weather_forecast.csv')
new_data = weather_solar
#print(new_data.columns)
weather = weather_solar#['prediction_num', 'datetime', 'Temp_Hi', 'Temp_Low', 'Cloud', 'Solar',
       #'Day', 'Month', 'windspeed', 'Direction']
#print(weather)

### UNCOMMENT TO MERGE INCOMING DATA WITH OLD DATA
#cd = os.path.dirname(os.path.abspath(__file__))

#old_weather_data = os.path.join(cd,'old_weather_forecast.csv')
#new_weather_data = os.path.join(cd,'new_weather_forecast.csv')

#filenames = old_weather_data, new_weather_data
#data = OrderedDict()
#fieldnames = []
#for filename in filenames:
    #with open(filename, 'r') as fp:
        #reader = csv.DictReader(fp)
        #fieldnames.extend(reader.fieldnames)
        #for row in reader:
            #data.setdefault(row['Day'], {}).update(row)
#fieldnames = list(OrderedDict.fromkeys(fieldnames))
#with open('merged.csv', 'w', newline='') as fp:
    #writer = csv.writer(fp)
    #writer.writerow(fieldnames)
    #for row in data.values():
        #writer.writerow([row.get(fields, '') for fields in fieldnames])

#new_data = pd.read_csv('merged.csv', index_col=[0])
#print(new_data)