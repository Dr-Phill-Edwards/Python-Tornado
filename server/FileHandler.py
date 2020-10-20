from tornado.web import StaticFileHandler

class FileHandler(StaticFileHandler):
    def initialize(self, path):
        self.absolute_path = False
        super(FileHandler, self).initialize(path)

    #def get(self, path = None, include_body = True):
    #    print('get ' + path)
    #    super(FileHandler, self).get(path, include_body)