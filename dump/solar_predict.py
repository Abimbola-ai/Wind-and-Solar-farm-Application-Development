import numpy as np
import pandas as pd
from datetime import date

def predictsolar(data):

	X = np.array(data[['Temp Hi', 'Temp Low', 'Solar', 'Cloud Cover Percentage', 'Rainfall in mm']])

	return X