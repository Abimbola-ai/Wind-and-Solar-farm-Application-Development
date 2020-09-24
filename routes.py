from flask import Flask, render_template, request, redirect
from flask import current_app as app
import pandas as pd
import csv
import os
from flask_wtf import Form
from weather_solar import *
from predict import round_data
from automate import final_merged_data
from merge import weather

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/GetWeatherData',methods = ['GET', 'POST'])
def mergedboth():
    return render_template('weather_data.html', tables=[weather.to_html(classes='data', index=False)], titles = ['na', 'Weather Data'])

@app.route('/Upload', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("Uploads", file.filename))
        return render_template('index.html',message="success")
    return render_template('index.html',message="Upload")


@app.route('/Predict', methods = ['GET','POST'])
def predict():
    return render_template('predict.html', tables=[round_data.to_html(classes='data', index=False)], titles = ['na', 'Predicted Values'])

@app.route('/Recalculate', methods = ['GET','POST'])
def calculate():
    return render_template('recalculate.html', tables=[final_merged_data.to_html(classes='data', index=False)], titles = ['na', 'Recalculated Values'])

