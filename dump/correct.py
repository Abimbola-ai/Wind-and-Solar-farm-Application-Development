from flask import Flask, render_template, request
import pandas as pd
import csv
import os

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("Uploads", file.filename))
        return render_template('index.html',message="success")
    return render_template('index.html',message="Upload")

if __name__ == '__main__':



import pandas as pd
import pickle
def updater:
       df1 = pd.read_csv('new_solar_data.csv', sep=",")
       df1['Temp Hi'] = df1['Temp Hi'].replace('\u00b0','', regex=True).astype(float)
       df1['Temp Low'] = df1['Temp Low'].replace('\u00b0','', regex=True).astype(float)


       #print(df1)
       df2 = pd.read_csv('solar_farm.csv', sep=",")
       #print(df2)

       df3 = df1.merge(df2, left_on = ['Day'], right_on = ['Date Of Month'], how = 'left')


       df3['Capacity Available'] = df3['Capacity Available'].fillna(100)


       df3["Estimated Power Generated MW"] = df3["Power Generated in MW"]* df3["Capacity Available"]/100

       #print(df3.head())
       solar_data = df3[['Month ', 'Day', 'Temp Hi', 'Temp Low', 'Solar',
       'Cloud Cover Percentage', 'Rainfall in mm','Estimated Power Generated MW']]

       print(solar_data.head())