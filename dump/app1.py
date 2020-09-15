import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model.

with open(f'solar_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():

    if flask.request.method == 'GET':

        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':

        #Day = flask.request.form['Day']
        Temp_Hi = flask.request.form['Temp Hi']
        Temp_Low = flask.request.form['Temp Low']
        Solar = flask.request.form['Solar']
        Cloud = flask.request.form['Cloud Cover Percentage']
        Rainfall = flask.request.form['Rainfall in mm']
        #Capacity = flask.request.form['Capacity']
        input_variables = pd.DataFrame([[Temp_Hi, Temp_Low, Solar, Cloud, Rainfall]],

                                       columns=['Temp Hi','Temp Low','Solar','Cloud Cover Percentage','Rainfall in mm'],

                                       dtype=float)

        prediction = model.predict(input_variables)[0]
        #newPower = prediction * Capacity/100
        return flask.render_template('main.html',

                                     original_input={'TempHi':Temp_Hi,

                                                     'TempLow':Temp_Low,

                                                     'Solar':Solar,

                                                     'Cloud':Cloud,

                                                     'Rainfall':Rainfall},

                                     result1=prediction

                                     )

if __name__ == '__main__':

    app.run(debug=True)