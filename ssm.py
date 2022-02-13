#ssm 

import pandas as pd
import seaborn as sns
import numpy as np
from flask import Flask

data = pd.read_excel(r'C:/Users/Owner/Downloads/fakeData.xlsx')


target = 'Miami'

city = data['City'].iloc[7]

avgRain = data['avgRain'].iloc[7]

currentRain = data['currentRain'].iloc[7]

groundWater = data['ground water level'].iloc[7]

soil = data['Soil'].iloc[7]

if (currentRain > avgRain) and (groundWater < 7) and (soil == 'Limestone'):
    print("At risk for sinkhole")
else:
    print('Not at risk for sinkhole')



app = Flask(__name__)


@app.route('/members')
def hello():
    return "<p>Hello, Jordyn!</p>"

