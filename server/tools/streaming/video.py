import socket
import base64
import datetime
import struct

class loc:
    def __init__(self, sock=8089):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', sock))
    def listen(self):
        self.sock.listen(10)
        conn, addr=self.sock.accept()
        payload_size = struct.calcsize("L")
        while True:
            data = b""
            while len(data) < payload_size:
                data += conn.recv(4096)
            pms = data[:payload_size]
            data = data[payload_size:]
            ms = struct.unpack("L", pms)[0]
            while len(data) < ms:
                data += conn.recv(4096)
            fdata = data[:ms]
            data = base64.decodestring(fdata)
            t = open("t.png", "wb")
            t.write(data)
            t.close()