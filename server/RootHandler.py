from tornado.web import RequestHandler

class RootHandler(RequestHandler):
    def get(self):
        self.write("Login")