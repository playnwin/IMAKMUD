from autobahn.twisted.websocket import WebSocketServerProtocol
from src.parser import parse

class MUDProtocol(WebSocketServerProtocol):
    query = ""

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        self.sendMessage("Enter your character name followed by your password, separated by a space.".encode("utf8"),
                         False)
        self.query = "login "

    def onMessage(self, payload, isBianary):
        message = "{}".format(self.query) + payload.decode('utf8')
        self.query = ""
        print("Got message: {}".format(message))
        response = parse(message)
        print("Making response: {}".format(response))
        self.sendMessage(response.encode("utf8"), False)
        if response == "Login unsuccessful. Have a nice day.":
            self.sendClose()
        elif response == "I couldn't find a character by that name.":
            self.sendMessage("Enter your character name followed by your password, "
                             "separated by a space.".encode("utf8"), False)
            self.query = "login "

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))
