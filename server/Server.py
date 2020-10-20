import sys
from tornado.httpserver import HTTPServer
from tornado.web import Application
from server.LoginHandler import LoginHandler
from server.RootHandler import RootHandler
from server.MessageWebSocket import MessageWebSocket
from server.FileHandler import FileHandler

class Server(Application):
   def __init__(self, port):
      super(Server, self).__init__([
         ("/", RootHandler),
         ("/login", LoginHandler),
         ("/wsmessage", MessageWebSocket),
         ('/client/(.*)', FileHandler, {'path': "client"})
      ])
      self.port = port
      self.http_server = HTTPServer(self)
      self.http_server.listen(port)
      print("Listening on port", port)
