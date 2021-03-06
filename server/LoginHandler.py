import os
import urllib
from okta_jwt.jwt import validate_token
from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler

class LoginHandler(RequestHandler):
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        self.set_header("Access-Control-Allow-Origin", "*")
        base_uri = self.get_argument("base_uri")
        client_id = self.get_argument("client_id")
        token = self.get_argument("token")
        try:
            response = validate_token(token, os.environ['OKTA_ISSUER_URI'], 'api://default', client_id)
            print(response)
            self.write("Welcome {}\n".format(email))
        except:
            self.send_error(403)
