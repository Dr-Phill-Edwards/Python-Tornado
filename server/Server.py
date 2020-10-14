import sys
from tornado.httpserver import HTTPServer
from tornado.web import Application
from server.RootHandler import RootHandler

class Server(Application):
   def __init__(self, port):
      super(Server, self).__init__([
         ("/", RootHandler),
      ])
      self.http_server = HTTPServer(self)
      self.http_server.listen(port)
      print("Listening on port", port)
