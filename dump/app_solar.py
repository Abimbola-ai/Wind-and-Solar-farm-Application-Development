import json, pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/predict_solar/', methods=['POST'])

def makecalc():
	jsonfile = request.get_json()
    data = pd.read_json(json.dumps(jsonfile),orient='index',convert_dates=['dteday'])
    print(data)
    res = dict()
    ypred = model.predict(predict_solar(data))
    for i in range(len(ypred)):
        res[i] = ypred[i]
    return jsonify(res) 

if __name__ == '__main__':

	modelfile = 'solar_model.pickle'    
    model = pickle.load(open(modelfile, 'rb'))
    print("loaded OK")

	app.run(debug=True)
