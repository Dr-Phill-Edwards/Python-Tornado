import sys
from server.Server import Server
from tornado.ioloop import IOLoop

lastarg = sys.argv[len(sys.argv) - 1]
port = int(lastarg) if lastarg.isnumeric() else 8888
application = Server(port)
IOLoop.current().start()
