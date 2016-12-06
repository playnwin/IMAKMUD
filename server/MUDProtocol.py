from autobahn.twisted.websocket import WebSocketServerProtocol
from src.parser import parse

class MUDProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))

        # echo back message verbatim
        message = payload.decode('utf8')
        print("Got message: {}".format(message))
        response = parse(message)
        print("Making response: {}".format(response))
        self.sendMessage(response.encode("utf8"), isBinary)
    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))
