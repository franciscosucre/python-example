# Standard libs imports
import os

# Local folder libs imports
from .requestHandler import RequestHandler


class StaticHandler(RequestHandler):
    def __init__(self: 'StaticHandler'):
        self.filetypes = {".js": "text/javascript", ".css": "text/css", ".jpg": "image/jpeg", ".png": "image/png", "notfound": "text/plain"}

    def find(self: 'StaticHandler', file_path: str) -> bool:
        split_path = os.path.splitext(file_path)
        extension = split_path[1]

        try:
            if extension in (".jpg", ".jpeg", ".png"):
                self.contents = open("public{}".format(file_path), 'rb')
            else:
                self.contents = open("public{}".format(file_path), 'r')

            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('notfound')
            self.setStatus(404)
            return False

    def setContentType(self: 'StaticHandler', ext: str) -> None:
        self.contentType = self.filetypes[ext]
