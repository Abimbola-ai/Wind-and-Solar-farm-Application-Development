from flask import Flask, render_template, request
import pandas as pd
import csv
import os
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
from flask_wtf import Form

engine = create_engine('sqlite:///new_data.db', echo=True)
sqlite_connection = engine.connect()
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("Uploads", file.filename))
        return render_template('index.html',message="success")
    return render_template('index.html',message="Upload")

if __name__ == '__main__':
    app.run(debug=True)