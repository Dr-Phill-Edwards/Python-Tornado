from tornado.web import RequestHandler

class LoginHandler(RequestHandler):
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        print(email, password)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write("Welcome {}\n".format(email))