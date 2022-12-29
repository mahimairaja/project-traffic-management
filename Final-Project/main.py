
from flask import Flask,render_template,Response, request, redirect, url_for, jsonify, make_response
from camera import *
from random import random
import pyrebase, time, pandas as pd, json, cv2
from dotenv import load_dotenv as ld
from os import environ
from json import loads
import sqlite3
import threading

app=Flask(__name__)

# TO load the environment variable
ld()  
config = loads(environ.get('config'))
# print(config)

# Connecting with Firebase
firebase = pyrebase.initialize_app(config)
database = firebase.database()

# Enpoint to render the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    writeData() # To write the data to database
    return render_template("chart.html")

# Enpoint that reads the last updated data in csv
@app.route('/data', methods=["GET", "POST"])
def data():
    # data = pd.read_csv('data/data.csv')
    db = sqlite3.connect('database/database.db')
    data = pd.read_sql('select * from signal',db)
    db.close()
    timeData = data['Time'].iloc[-1]  # Time data 
    y1 = int(data['lane_1'].iloc[-1]) # Lane 1 car count
    y2 = int(data['lane_2'].iloc[-1]) # Lane 2 car count
    y3 = int(data['lane_3'].iloc[-1]) # Lane 3 car count
    y4 = int(data['lane_4'].iloc[-1]) # Lane 4 car count
    data1 = [timeData, y1]
    data2 = [timeData, y2]
    data3 = [timeData, y3]
    data4 = [timeData, y4]

    data = list((data1,data2,data3,data4))
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

# Endpoint that renders the camera page
@app.route('/home')
def home():
    writeData()
    return render_template("camera.html")

#Endpoint for camera 01
@app.route('/video')
def video():
    # Do pass the camera path in genenarate frames as parameter
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

#Endpoint for camera 02
@app.route('/video2')
def video2():
    # Do pass the camera path in genenarate frames as parameter
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

#Endpoint for camera 03
@app.route('/video3')
def video3():
    # Do pass the camera path in genenarate frames as parameter
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

#Endpoint for camera 04
@app.route('/video4')
def video4():
    # Do pass the camera path in genenarate frames as parameter
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

# Reads the csv and update the firebase for every 10 seconds
def writeData():
    threading.Timer(10.0, writeData).start()  
    # data = pd.read_csv('data/data.csv')
    db = sqlite3.connect('database/database.db')
    data = pd.read_sql('select * from signal',db)
    db.close()
    curr_time = data['Time'].iloc[-1] # Time data
    y1 = int(data['lane_1'].iloc[-1]) # lane 1 car count 
    y2 = int(data['lane_2'].iloc[-1]) # Lane 2 car count 
    y3 = int(data['lane_3'].iloc[-1]) # Lane 3 car count
    y4 = int(data['lane_4'].iloc[-1]) # Lane 4 car count
    data = {"lane1" : y1, "lane2" : y2, "lane3" : y3, "lane4" : y4}
    database.child("Signal-01").child(curr_time).set(data)   
    # To debug let us print the data
    print("---* ---* ---*")
    print(data)


if __name__=="__main_":
    app.run(host='0.0.0.0')
