from tools.threads import video
from pages import *
import tornado.ioloop
import tornado.web

# Instantiate
vt = video.basic()
# Start
vt.start()

def make_app():
    return tornado.web.Application([
        (r"/", index.Handler),
        (r"/cin", cin.Handler),
        (r"/cameras", cameras.Handler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()