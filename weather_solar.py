# Code to get weather data
import os,csv
import time
import requests
import pandas as pd
from datetime import datetime
import time, calendar

apikey = os.environ.get('apikey')
lat = 19.9208
long = 142.1582


coord_API_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
join_key = "&exclude=current,minutely,hourly&appid=" + apikey
units = "&units=imperial"
forecast_coord_weather_url= coord_API_endpoint + lat_long + join_key + units
#print(forecast_coord_weather_url)

json_data = requests.get(forecast_coord_weather_url).json()
#print(json_data)

weather_solar = pd.DataFrame() #Create an empty dataframe


# Create an empty list to store in the DF
prediction_num = 0
list_pred_num = []
datetime = []
timezone = []
Temp_Hi = []
timezone = []
Temp_Low = []
Solar = []
Cloud = []
Rainfall = []

#Add json data to the list
for num_forecasts in json_data['daily']:
    weather_solar['prediction_num'] = prediction_num
    list_pred_num.append(prediction_num)
    datetime.append(json_data['daily'][prediction_num]['dt'])
    Temp_Hi.append(json_data['daily'][prediction_num]['temp']['max'])
    Temp_Low.append(json_data['daily'][prediction_num]['temp']['min'])
    Cloud.append(json_data['daily'][prediction_num]['clouds'])
    Solar.append(json_data['daily'][prediction_num]['uvi'])
    #Rainfall.append(json_data['daily'][prediction_num]['rain'])
    prediction_num += 1

#Write list to DF
weather_solar['prediction_num'] = list_pred_num
weather_solar['datetime'] = datetime
weather_solar['Temp_Hi'] = Temp_Hi
weather_solar['Temp_Low'] = Temp_Low
weather_solar['Cloud'] = Cloud
weather_solar['Solar'] = Solar
#weather_solar['Rainfall'] = Rainfall


# Convert timestamp to datetime
weather_solar['datetime'] = pd.to_datetime(weather_solar['datetime'], unit='s')
weather_solar['Day'] = weather_solar['datetime'].dt.day 
weather_solar['Month'] = weather_solar['datetime'].dt.month
weather_solar['Cloud'] = weather_solar['Cloud']/12.5
#weather_solar['Month'] = calendar.month_name(weather_solar['Month'])
#weather_solar.to_csv('new_solar_weather_forecast.csv')

#print(weather_solar)
#print(len(weather))