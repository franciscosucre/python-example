# Standard libs imports
import os
from http.server import BaseHTTPRequestHandler
import typing

# Third party libs imports
from routes.main import routes

from response.requestHandler import RequestHandler
from response.staticHandler import StaticHandler
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self: 'Server') -> None:
        return

    def do_GET(self: 'Server') -> None:
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]
        handler: RequestHandler
        if request_extension is "" or request_extension is ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                handler = BadRequestHandler()
        elif request_extension is ".py":
            handler = BadRequestHandler()
        else:
            handler = StaticHandler()
            handler.find(self.path)

        self.respond({'handler': handler})

    def handle_http(self: 'Server', handler: RequestHandler) -> bytes:
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"

        self.end_headers()

        return bytes(content, 'UTF-8')

    def respond(self: 'Server', opts: typing.Dict[str, RequestHandler]) -> None:
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)
