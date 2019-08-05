class MockFile():
    def read(self: 'MockFile') -> bool:
        return False


class RequestHandler():
    def __init__(self: 'RequestHandler'):
        self.contentType = ""
        self.contents = MockFile()

    def getContents(self: 'RequestHandler') -> bool:
        return self.contents.read()

    def read(self: 'RequestHandler') -> MockFile:
        return self.contents

    def setStatus(self: 'RequestHandler', status: int) -> None:
        self.status = status

    def getStatus(self: 'RequestHandler') -> int:
        return self.status

    def getContentType(self: 'RequestHandler') -> str:
        return self.contentType

    def getType(self: 'RequestHandler') -> str:
        return 'static'
