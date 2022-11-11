import cv2


camID = '/dev/video0'
camID2 = '/dev/video2'
camID3 = '/dev/video4'
camID4 = '/dev/video6'



def generate_frames(camID):
    camera=cv2.VideoCapture(camID)
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


