import sys
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from server.RootHandler import RootHandler
from server.LoginHandler import LoginHandler
from server.MessageWebSocket import MessageWebSocket
from server.FileHandler import FileHandler

define("port", default=8080, help="Listener port")
options.parse_command_line()
application = Application([
                 ("/", RootHandler),
                 ("/login", LoginHandler),
                 ("/wsmessage", MessageWebSocket),
                 ('/client/(.*)', FileHandler, {'path': "client"})
              ])
http_server = HTTPServer(application)
http_server.listen(options.port)
print("Listening on port", options.port)
IOLoop.current().start()
