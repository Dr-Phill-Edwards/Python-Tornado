import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from server.RootHandler import RootHandler

if __name__ == "__main__":
   application = Application([
         ("/", RootHandler),
      ])
   port = int(os.environ.get("PORT", 8888))
   application.listen(port)
   print("Running on port", port)
   IOLoop.current().start()
