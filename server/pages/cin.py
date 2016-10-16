from handlers import basic
import os
import base64

class Handler(basic.Handler):
    def postgen(self, arguments):
        self.cr()
        camera = str(arguments["cam"][0].decode())
        b64 = arguments["b64"][0]
        if os.path.exists("cameras/" + camera) != True:
            os.makedirs("cameras/" + camera)
        data = base64.decodestring(b64)
        t = open("cameras/{0}/t.png".format(camera), "wb")
        t.write(data)
        t.close()
        doc, tag, text = self.yat
        with tag("html"):
            with tag("body"):
                text("Hello world!")
        return doc.getvalue()