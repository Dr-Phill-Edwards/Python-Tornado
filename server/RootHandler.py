from tornado.web import RequestHandler

class RootHandler(RequestHandler):
    def get(self):
        self.write("Welcome to Tornado\n")

