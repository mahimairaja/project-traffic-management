import pandas as pd
import sqlite3
import time

db = sqlite3.connect('database.db')
data = pd.read_sql('select * from signal',db)

print(data)
print(type(data))
print(data.dtypes)

while True :
    timeData = data['Time'].iloc[-1]  # Time data 
    y1 = int(data['lane_1'].iloc[-1]) # Lane 1 car count
    y2 = int(data['lane_2'].iloc[-1]) # Lane 2 car count
    y3 = int(data['lane_3'].iloc[-1]) # Lane 3 car count
    y4 = int(data['lane_4'].iloc[-1])
    print(timeData, y1, y2, y3, y4)
    time.sleep(3)