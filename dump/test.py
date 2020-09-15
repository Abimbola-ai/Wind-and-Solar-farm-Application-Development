import pandas as pd
import csv

rows = {}
with open('new_solar_data.csv"', 'r', newline='') as acsv:
    areader = csv.DictReader(acsv)
    for row in reader:
        # store the row based on the item1 and item2 columns
        key = (row['Day']
        rows[key] = rows

with open('solar_farm.csv', 'r', newline='') as bcsv:
    breader = csv.DictReader(bcsv)
    for row in reader:
        # set the label of matching rows to 1 when present
        key = (row['Day'])
        if key in rows:
            rows[key]['newPower'] = row['Power']*row['Capacity']/100

with open('result.csv', 'w', newline='') as result:
    writer = csv.DictReader(result, fieldnames=areader.fieldnames)
    writer.writerows(rows.values())

PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE Weather_predict RENAME TO Predict;

sql_command = """ CREATE TABLE solar(
    Solar_id BIGINT,
    Days BIGINT PRIMARY KEY,
	Capacity BIGINT, 
	);"""


sql_command = """ CREATE TABLE wind_farm(
    Wind_id BIGINT,
    Days BIGINT PRIMARY KEY,
	Capacity BIGINT);"""
sql_command = """ CREATE TABLE weather(
    prediction_num INT PRIMARY KEY, 
    datetime TIMESTAMP, 
	Temp_Hi FLOAT, 
	Temp_Low FLOAT, 
	Cloud BIGINT, 
	Solar FLOAT, 
	windspeed FLOAT, 
	Direction BIGINT, 
	Rainfall FLOAT, 
	Day BIGINT, 
	Month BIGINT, 
	Power_Solar FLOAT(4,2), 
	Power_Wind FLOAT(4,2));"""

    sql_command = """ CREATE TABLE weather_wind(
    id INT PRIMARY KEY, 
	Temp_Hi FLOAT, 
	Temp_Low FLOAT, 
	Cloud BIGINT, 
	Solar FLOAT, 
	windspeed FLOAT, 
	Direction BIGINT, 
	Rainfall FLOAT, 
	Day BIGINT, 
	Month BIGINT, 
	Power_Solar FLOAT(4,2), 
	Power_Wind FLOAT(4,2),
    FOREIGN KEY(Day) REFERENCES wind_farm(Days));"""

sql_command = """ CREATE TABLE solar_farm(
    Solar_id BIGINT,
    Days BIGINT PRIMARY KEY,
	Capacity BIGINT 
	);"""

sql_command = """ CREATE TABLE wind(
    Wind_id BIGINT,
    Days BIGINT PRIMARY KEY,
	Capacity BIGINT);"""