# server.py
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

camera = cv2.VideoCapture(0)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    """video straming rout. put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


def gen():
    while True:
        success, frame = camera.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@socketio.on("connect")
def handle_connect():
    emit("chat", "Connected to server")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


@socketio.on("message")
def handle_message(msg):
    emit("chat", msg, broadcast=True)  # 모든 클라이언트에게 메시지를 보냄


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=9001)
