import typing

# Local folder libs imports
from .requestHandler import RequestHandler


class TemplateHandler(RequestHandler):
    def __init__(self: 'TemplateHandler'):
        super().__init__()
        self.contentType = 'text/html'

    def find(self: 'TemplateHandler', routeData: typing.Dict[str, str]) -> bool:
        try:
            template_file = open('templates/{}'.format(routeData['template']))
            self.contents = template_file
            self.setStatus(200)
            return True
        except:
            self.setStatus(404)
            return False
