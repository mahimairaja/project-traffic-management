from flask import Flask,render_template,Response, request, redirect, url_for, jsonify, make_response
from camera import *
from random import random
import pyrebase, time, pandas as pd, json, cv2
from dotenv import load_dotenv as ld
from os import environ
from json import loads
import threading

app=Flask(__name__)

ld()
config = loads(environ.get('config'))
print(config)

firebase = pyrebase.initialize_app(config)
database = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def index():
    writeData()
    return render_template("chart.html")

@app.route('/data', methods=["GET", "POST"])
def data():
    data = pd.read_csv('data/data.csv')
    timeData = data['Time'].iloc[-1]
    y1 = int(data['lane_1'].iloc[-1])
    y2 = int(data['lane_2'].iloc[-1])
    y3 = int(data['lane_3'].iloc[-1])
    y4 = int(data['lane_4'].iloc[-1])
    data1 = [timeData, y1]
    data2 = [timeData, y2]
    data3 = [timeData, y3]
    data4 = [timeData, y4]

    data = list((data1,data2,data3,data4))
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/home')
def home():
    writeData()
    return render_template("camera.html")


@app.route('/video')
def video():
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2')
def video2():
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video3')
def video3():
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video4')
def video4():
    return Response(generate_frames(0),mimetype='multipart/x-mixed-replace; boundary=frame')

def writeData():
    threading.Timer(5.0, writeData).start()   # For every 5 seconds data in retrived ! 
    data = pd.read_csv('data/data.csv')
    x = data['Time'].iloc[-1]
    y1 = int(data['lane_1'].iloc[-1])
    y2 = int(data['lane_2'].iloc[-1])
    y3 = int(data['lane_3'].iloc[-1])
    y4 = int(data['lane_4'].iloc[-1])
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    data = {"lane1" : y1, "lane2" : y2, "lane3" : y3, "lane4" : y4}
    print("---* ---* ---*")
    print(data)
    # database.child("Signal-01").child(curr_time).set(data)   # Uncomment to upload to database ! 

if __name__=="__main_":
    app.run(host='0.0.0.0')


