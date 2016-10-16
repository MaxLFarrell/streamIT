import cv2
import socket
import base64
import struct
import requests

class Streamer:
    def __init__(self, cam=0, sock=8089):
        self.cap = cv2.VideoCapture(cam)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect(('localhost', sock))
    def stream(self):
        while True:
            frame =self.cap.read()[1]
            data = cv2.imencode('.png', frame)[1]
            data = base64.b64encode(data)
            data = {
                "b64":data,
                "cam":"dog"
            }
            r = requests.post("http://127.0.0.1:8888/cin", data=data)
            print(r.text)