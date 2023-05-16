from flask import Flask,render_template,url_for,Response
#pip install opencv-python
import cv2

app = Flask(__name__)
#To access webcam, we need to create a VideoCapture object, add 0 for webcam
camera = cv2.VideoCapture(0)

def generate_frames():

    while True:
        success,frame = camera.read() #returns a tuple, first value is a boolean, second is the frame (if true then read the frame)

        if not success:
            break
        else:
            #encode the image into jpeg format
            ret,buffer = cv2.imencode('.jpg',frame)
            #convert the image/buffer into bytes
            frame = buffer.tobytes()
        #We can't use return as it will just return 1 frame, so to go back to first step, we use "yield" along with the generator function
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


if(__name__) == '__main__':
    app.run(debug=True)