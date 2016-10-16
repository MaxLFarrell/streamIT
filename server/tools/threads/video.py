from tools.streaming import video
import threading

class basic (threading.Thread):
    def __init__(self, sock=None):
        threading.Thread.__init__(self)
        if sock == None:
            sock = 8089
        self.vs = video.loc(sock=sock)
    def run(self):
        self.vs.listen()