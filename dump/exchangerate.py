import os
import io
import time
import requests
import pandas as pd

exchange_url = "https://api.exchangeratesapi.io/latest?base=USD"
json_data = requests.get(exchange_url).json()

print(json_data)
