from flask import Flask,render_template,Response, request, redirect, url_for
import cv2
from camera import *
from firebase import config
import pyrebase
import datetime
import time


app=Flask(__name__)

firebase = pyrebase.initialize_app(config)
database = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html') # , result=10

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        lane1 = request.form['lane1']
        lane2 = request.form['lane2']
        lane3 = request.form['lane3']
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        data = {"lane1" : lane1, "lane2" : lane2, "lane3" : lane3}
        database.child("Signals").child(curr_time).set(data)
        print(data)
        return render_template('count.html')
    else:
        return render_template('count.html')

@app.route('/<lan1>')
def user(lan1):
    return f"<h1>Lane 1 : {lan1}</h1><h1>Lane 1 : {lan1}</h1><h1>Lane 1 : {lan1}</h1>"

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
    app.run(debug=True)
