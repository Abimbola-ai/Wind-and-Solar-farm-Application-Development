#!/usr/bin/python
import sqlite3
connection = sqlite3.connect('weather_data.db')
cursor = connection.cursor()

#sql_command = """ PRAGMA foreign_keys=off;"""

#sql_command = """ BEGIN TRANSACTION; """

#sql_command = """ALTER TABLE Solar_maintenance RENAME TO sm;"""

#sql_command = """ CREATE TABLE Solar_maintenance(
    Solar_id BIGINT,
    Days BIGINT ,
	Capacity BIGINT, 
    CONSTRAINT Solar_maintenace_pk PRIMARY KEY (Days)
	);"""
#sql_command = """INSERT INTO Solar_maintenance  SELECT * FROM sm;"""
sql_command ="""COMMIT;"""

cursor.execute(sql_command)
result = cursor.fetchall()
print (result)




