import os
import time
import requests
import pandas as pd

apikey = "59394d25f1a78085f076c9d0ab6cf23c"
lat = 6.4474
long = 3.3903
coord_API_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
lat_long = "lat=" + str(lat)+ "&lon=" + str(long)
join_key = "&exclude=current,minutely,hourly&appid=" + apikey
units = "&units=metric"
forecast_coord_weather_url= coord_API_endpoint + lat_long + join_key + units
#print(forecast_coord_weather_url)

json_data = requests.get(forecast_coord_weather_url).json()
print(json_data)





