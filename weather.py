# Code to get weather data
import os,csv
import time
import requests
import pandas as pd
from datetime import datetime
import time, calendar

apikey = "59394d25f1a78085f076c9d0ab6cf23c"
lat = 6.4474
long = 3.3903
#IP_url = "http://ip-api.com/json"

coord_API_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
join_key = "&exclude=current,minutely,hourly&appid=" + apikey
units = "&units=metric"
forecast_coord_weather_url= coord_API_endpoint + lat_long + join_key + units
#print(forecast_coord_weather_url)

json_data = requests.get(forecast_coord_weather_url).json()
print(json_data)

weather = pd.DataFrame() #Create an empty dataframe


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
windspeed = []
Direction = []

#Add json data to the list
for num_forecasts in json_data['daily']:
    weather['prediction_num'] = prediction_num
    list_pred_num.append(prediction_num)
    datetime.append(json_data['daily'][prediction_num]['dt'])
    #if json_data['city']['timezone'] >0:
        #timezone.append(("+" +str((json_data['city']['timezone'])/3600)))
    #else:
        #timezone.append(((json_data['city']['timezone'])/3600))
    Temp_Hi.append(json_data['daily'][prediction_num]['temp']['max'])
    Temp_Low.append(json_data['daily'][prediction_num]['temp']['min'])
    Cloud.append(json_data['daily'][prediction_num]['clouds'])
    windspeed.append(json_data['daily'][prediction_num]['wind_speed'])
    Direction.append(json_data['daily'][prediction_num]['wind_deg'])
    Solar.append(json_data['daily'][prediction_num]['uvi'])
    #Rainfall.append(json_data['daily'][prediction_num]['rain'])
    prediction_num += 1

#Write list to DF
weather['prediction_num'] = list_pred_num
weather['datetime'] = datetime
weather['Temp_Hi'] = Temp_Hi
weather['Temp_Low'] = Temp_Low
weather['Cloud'] = Cloud
weather['Solar'] = Solar
weather['windspeed'] = windspeed
weather['Direction'] = Direction
#weather['Rainfall'] = Rainfall


# Convert timestamp to datetime
weather['datetime'] = pd.to_datetime(weather['datetime'], unit='s')
weather['Day'] = weather['datetime'].dt.day 
weather['Month'] = weather['datetime'].dt.month
#weather['Month'] = calendar.month_name(weather['Month'])
weather.to_csv('new_weather_forecast.csv')

#print(weather.head())
#print(len(weather))



