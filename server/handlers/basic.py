from bs4 import BeautifulSoup
import tornado.web
from yattag import Doc

class Handler(tornado.web.RequestHandler):
    def cr(self):
        self.yat = Doc().tagtext()
    def getgen(self, arguments):
        return ""
    def get(self):
        res = self.getgen(self.request.arguments)
        soup = BeautifulSoup(res, "html.parser")
        self.write(soup.prettify())
    def postgen(self, arguments):
        return ""
    def post(self):
        res = self.postgen(self.request.arguments)
        soup = BeautifulSoup(res, "html.parser")
        self.write(soup.prettify())