import sys
from server.Server import Server
from tornado.ioloop import IOLoop
from tornado.options import define, options

define("port", default=8888, help="Listener port")
application = Server(options.port)
IOLoop.current().start()
