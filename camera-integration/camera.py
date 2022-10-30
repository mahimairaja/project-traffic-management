import cv2


camID = '/dev/video0'
camID2 = '/dev/video2'
camID3 = '/dev/video4'
camID4 = '/dev/video6'

camera=cv2.VideoCapture(camID, cv2.CAP_V4L2)

def generate_frames():
    while True:
           
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

camera2=cv2.VideoCapture(camID2, cv2.CAP_V4L2)

def generate_frames2():
    while True:
           
        ## read the camera frame
        success,frame=camera2.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

camera3=cv2.VideoCapture(camID3, cv2.CAP_V4L2)

def generate_frames3():
    while True:
           
        ## read the camera frame
        success,frame=camera3.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
camera4=cv2.VideoCapture(camID4, cv2.CAP_V4L2)

def generate_frames4():
    while True:
           
        ## read the camera frame
        success,frame=camera4.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')