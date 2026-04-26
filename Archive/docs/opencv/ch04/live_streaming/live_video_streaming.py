from flask import Flask, Response, request, render_template
import cv2
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

cascade_filename = (
    "C:\\MyMoble\\OpenCV\\opencv\\data\\haarcascades\\haarcascade_frontalface_alt.xml"
)
cascade = cv2.CascadeClassifier(cascade_filename)


def imgDetector(img, cascade):
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = cascade.detectMultiScale(
        gray,  # 입력 이미지
        scaleFactor=1.1,  # 이미지 피라미드 스케일 factor
        minNeighbors=2,  # 인접 객체 최소 거리 픽셀
        minSize=(20, 20),  # 탐지 객체 최소 크기
    )

    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

    return img


def gen():
    camera = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    camera.set(3, 640)
    camera.set(4, 480)
    while 1:
        _, frame = camera.read()
        retimg = imgDetector(frame, cascade)
        cv2.imwrite("pic.jpg", retimg)
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + open("pic.jpg", "rb").read() + b"\r\n"
        )
    camera.release()
    cv2.destroyAllWindows()


@socketio.on("connect")
def handle_connect():
    print("Client connected")
    socketio.emit("connection_response", {"data": "Connected"})


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


@socketio.on("message")
def handle_message(text):
    socketio.emit("chat", text)


@app.route("/")
def index():
    """Video streaming ."""
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    """video straming rout. put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run("0.0.0.0", port=9000, debug=True, threaded=True)
