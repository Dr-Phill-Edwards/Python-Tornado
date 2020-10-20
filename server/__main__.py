import sys
from server.Server import Server
from tornado.ioloop import IOLoop
from tornado.options import define, options

define("port", default=8888, help="Listener port")
options.parse_command_line()
application = Server(options.port)
IOLoop.current().start()
