from flask import Flask,render_template,Response
import cv2
from camera import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2')
def video2():
    return Response(generate_frames2(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video3')
def video3():
    return Response(generate_frames3(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video4')
def video4():
    return Response(generate_frames4(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main_":
    app.run(debug=True)
