import pandas as pd
import numpy as np
#from predict import new_data

wind_data = pd.read_csv('~/Documents/AIIP/AppDev/Summative/Uploads/wind_farm.csv', index_col=None)
solar_data = pd.read_csv('~/Documents/AIIP/AppDev/Summative/Uploads/solar_farm.csv', index_col=None)
wind_data = wind_data.apply(pd.to_numeric, errors='coerce')
solar_data = solar_data.apply(pd.to_numeric, errors='coerce')