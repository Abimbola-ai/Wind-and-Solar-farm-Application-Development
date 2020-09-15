from flask import Flask, request, jsonify
import csv
from update_solar import updater

app = Flask(__name__)

@app.route("/update",methods=["POST"])
def calc():
    data = pd.read_csv("./solar_generation_data.csv")
    data ['Power'] = data(updater)
 
    return data
# Running the server in localhost:5000 
if __name__ == "__main__":
 app.run(debug=True)



 def database(Days, Capacity):
    conn = sqlite3.connect("new_data.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXIXTS wind_maintenance (Days BIGINT, Capacity BIGINT) """)
    cursor.execute(""" INSERT INTO wind_maintenance (Days, Capacity) VALUE (?,?)""", (Days,Capacity))
    conn.commit()
    cursor.close()
    conn.close()