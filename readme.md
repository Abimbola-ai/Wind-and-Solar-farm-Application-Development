### Application Development
This project predicts the output power for a client that has both solar and wind power plants. 

Both these farms feed their output electrical energy to the local grid where they are located. Our aim is to produce an application that is able to predict the amount of power we expect to generate on a day in the near future in order to provide this information to the grid operator. The information to be used to generate this model will include:

Weather conditions (sunshine, wind speed, cloud cover etc)
Maintenance schedules (see CSV files in the resources section) can be uploaded
The effect of the weather on the electrical energy outputs should be determined by looking at the historical data. During maintenance, some part of the plant is down. Therefore, when 30% of the plant is undergoing maintenance, for instance, the maximum capacity it can generate with ideal weather conditions is only 70% of its actual maximum.

The following task were carried out:

* Create an architecture for your application (a simple block diagram showing the core functions)
* Create a simple ML model which accepts suitable inputs and gives a predicted power output for each power generation plant for any day within the next 7 days. Note that these may be 2 ML models (1 for each plant) 
* Store this ML model as a file so you can save it to use later (or in another computer).pkl and wind_model.pkl
* Create an API endpoint that allows upload of a CSV file to change the maintenance schedule being used - 
* Include application logic that takes this predicted output and uses the maintenance schedule to scale the production capacity appropriately. For instance, if the predicted power output for the wind farm is 7 MW for a particular day but on that day of the month we expect to have 30% of the wind farm undergoing maintenance, the actual output will be 0.7*7 = 4.9 MW as the wind farm will be operating at 70% capacity 
 
* Create a dashboard that will:
    1. Display the expected power output for both plants on each of the 4 consecutive days. (tomorrow, day after, day after that and the day after the day after that :) )
    2. Have a button which when pressed would cause a summary of this forecast to be sent to a phone number of your choice as an SMS using Twilio. (optional for extra credit)

### The following files were developed the solve the problem
solar.py and wind.py -  Create a model that predicts output power using simple linear regression
solar_model.pkl and wind_model.pkl - store the models in a pickle
weather_solar.py/weather_wind.py - Collect weather data based on the location
merge.py - merges the Solar weather data to that of the wind weather data
predict.py - Predict the new data for wind and solar
automate.py - perform updates of the power output based on the maintenance schedule uploaded
routes.py -  create a flask application that uploads csv to the database,interacts with the predicted data etc.
dashboard.py  - create dashboard to show the data
test_whatsapp.py - twilio sms sending 
__init__.py -  Combines the flask routes and the dash app incorporated into flask
wsgi.py -  Application entry point for the entire application Development

### Instructions 
Clone Repsoitory and then run wsgi.py