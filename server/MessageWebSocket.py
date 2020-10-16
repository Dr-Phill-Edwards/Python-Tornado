from tornado.websocket import WebSocketHandler

class MessageWebSocket(WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("Message Web Socket Opened")
        self.counter = 1

    def on_message(self, message):
        self.write_message("Message " + str(self.counter) + ': ' + message)
        self.counter += 1

    def on_close(self):
        print("Message Web Socket Closed")
