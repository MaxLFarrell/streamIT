from handlers import basic
import os

class Handler(basic.Handler):
    def get(self):
        self.cr()
        camera = self.request.arguments["cam"][0].decode()
        self.set_header("Content-type",  "image/png")
        self.write(open("cameras/{0}/t.png".format(camera), "rb").read())