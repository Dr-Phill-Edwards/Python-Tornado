import sys
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from server.RootHandler import RootHandler

class Server(Application):
   def __init__(self, port):
      super(Server, self).__init__([
         ("/", RootHandler),
      ])
      self.listen(port)
      print("Listening on port", port)

if __name__ == "__main__":
   lastarg = sys.argv[len(sys.argv) - 1]
   port = int(lastarg) if lastarg.isnumeric() else 8888
   application = Server(port)
   IOLoop.current().start()
