import cv2

# Here the path for camera is defined as of Macintosh
# Do change the path accordingly in main function 

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
        # The video is rendered as sequence of images as bytes stream
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


