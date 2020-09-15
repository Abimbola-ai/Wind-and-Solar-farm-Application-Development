from flask import Flask, render_template, request
import pandas as pd
import csv
import os
from update_solar import updater

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("Uploads", file.filename))
        return render_template('index.html',message="success")
    return render_template('index.html',message="Upload")

@app.route('/update', methods = ['POST'])
def update():
    if request.method =='POST':
        f = request.

if __name__ == '__main__':
    app.run(debug=True)
