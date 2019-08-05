# Local folder libs imports
from .requestHandler import RequestHandler


class BadRequestHandler(RequestHandler):
    def __init__(self: 'BadRequestHandler'):
        super().__init__()
        self.contentType = 'text/plain'
        self.setStatus(404)
