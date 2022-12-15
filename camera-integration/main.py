from flask import Flask,render_template,Response, request, redirect, url_for, jsonify, make_response
import cv2
from camera import *
from random import random
import pyrebase
import time
import json
from dotenv import load_dotenv as ld
from os import environ
from json import loads

app=Flask(__name__)

ld()
config = loads(environ.get('config'))
print(config)

firebase = pyrebase.initialize_app(config)
database = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        l1 = request.form.get("lane1")
        l2 = request.form.get("lane2")  
        l3 = request.form.get("lane3")
        l4 = request.form.get("lane4")
        
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        data = {"lane1" : l1, "lane2" : l2, "lane3" : l3, "lane4" : l4}
        database.child("Signal-01").child(curr_time).set(data)
        return jsonify(Lane1 = l1, Lane2 = l2, Lane3 = l3, Lane4 = l4 )
    return render_template("chart.html")

@app.route('/data', methods=["GET", "POST"])
def data():
    data1 = [time.strftime("%H:%M:%S", time.localtime()), random() * 100]
    data2 = [time.strftime("%H:%M:%S", time.localtime()), random() * 100]
    data3 = [time.strftime("%H:%M:%S", time.localtime()), random() * 100]
    data4 = [time.strftime("%H:%M:%S", time.localtime()), random() * 100]

    data = list((data1,data2,data3,data4))
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/dashboard')
def dash():
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

if __name__=="__main_":
    app.run(host='0.0.0.0')
