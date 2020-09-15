#!/usr/bin/python
import sqlite3
connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

sql_command = """SELECT * FROM wind_farm
;"""


cursor.execute(sql_command)
result = cursor.fetchall()
print (result)
