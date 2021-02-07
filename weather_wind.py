# Code to get weather data
import os,csv
import time
import requests
import pandas as pd
from datetime import datetime
import time, calendar

#apikey = os.environ.get('apikey')
lat = 27.9881
long = 86.9250


coord_API_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
join_key = "&exclude=hourly&appid=" + "xxxxx" #input your api key in xxxxx
units = "&units=imperial"
forecast_coord_weather_url= coord_API_endpoint + lat_long + join_key + units
#print(forecast_coord_weather_url)

json_data = requests.get(forecast_coord_weather_url).json()
weather_wind = pd.DataFrame() #Create an empty dataframe


# Create an empty list to store in the DF
prediction_num = 0
list_pred_num = []
datetime = []
#timezone = []
#Temp_Hi = []
#timezone = []
#Temp_Low = []
#Solar = []
#Cloud = []
#Rainfall = []
windspeed = []
Direction = []

#Add json data to the list
for num_forecasts in json_data['daily']:
    weather_wind['prediction_num'] = prediction_num
    list_pred_num.append(prediction_num)
    datetime.append(json_data['daily'][prediction_num]['dt'])
    #if json_data['city']['timezone'] >0:
        #timezone.append(("+" +str((json_data['city']['timezone'])/3600)))
    #else:
        #timezone.append(((json_data['city']['timezone'])/3600))
    #Temp_Hi.append(json_data['daily'][prediction_num]['temp']['max'])
    #Temp_Low.append(json_data['daily'][prediction_num]['temp']['min'])
    #Cloud.append(json_data['daily'][prediction_num]['clouds'])
    windspeed.append(json_data['daily'][prediction_num]['wind_speed'])
    Direction.append(json_data['daily'][prediction_num]['wind_deg'])
    #Solar.append(json_data['daily'][prediction_num]['uvi'])
    #Rainfall.append(json_data['daily'][prediction_num]['rain'])
    prediction_num += 1

#Write list to DF
weather_wind['prediction_num'] = list_pred_num
weather_wind['datetime'] = datetime
#weather['Temp_Hi'] = Temp_Hi
#weather['Temp_Low'] = Temp_Low
#weather['Cloud'] = Cloud
#weather['Solar'] = Solar
weather_wind['windspeed'] = windspeed
weather_wind['Direction'] = Direction
#weather['Rainfall'] = Rainfall


# Convert timestamp to datetime
weather_wind['datetime'] = pd.to_datetime(weather_wind['datetime'], unit='s')
weather_wind['Day'] = weather_wind['datetime'].dt.day 
weather_wind['Month'] = weather_wind['datetime'].dt.month
#weather['Month'] = calendar.month_name(weather['Month'])
#weather_wind.to_csv('new_wind_weather_forecast.csv')

#print(weather_wind)
#print(len(weather))