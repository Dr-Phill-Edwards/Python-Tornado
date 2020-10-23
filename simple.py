from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

class SimpleHandler(RequestHandler):
    def get(self):
        self.write("Welcome to Tornado!")

app = Application([('/', SimpleHandler)])
app.listen(8080)
print('Listening')
IOLoop.current().start()