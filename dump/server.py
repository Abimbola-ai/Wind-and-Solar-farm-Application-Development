import sqlite3
from upload import wind_data, solar_data
from predict import new_data
from sqlite3 import Error
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///weather_data.db', echo=True)
sqlite_connection = engine.connect()
def create_connection(path):
    connection = create_connection("database.sqlite")
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e} occured")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")

sqlite_table = 'weather_solar'
new_data.to_sql(sqlite_table, sqlite_connection, if_exists='replace', index=False)

sqlite_table = 'weather_wind'
new_data.to_sql(sqlite_table, sqlite_connection, if_exists='replace', index=False)

sqlite_table = 'wind_farm'
wind_data.to_sql(sqlite_table, sqlite_connection, if_exists='replace', index=False)

sqlite_table = 'solar_farm'
solar_data.to_sql(sqlite_table, sqlite_connection, if_exists='replace', index=False)



sqlite_connection.close()