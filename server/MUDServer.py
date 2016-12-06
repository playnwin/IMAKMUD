from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from src.parser import parse
from src import world


class MUDProtocol(WebSocketServerProtocol):
    query = ""
    name = ""

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        self.factory.register(self)
        self.sendMessage("Enter your character name: ".encode("utf8"), False)
        self.query = "login_u "

    def onMessage(self, payload, isBianary):
        message = "{}".format(self.query) + payload.decode('utf8')
        print("Got message: {}".format(message))
        response = parse(message)
        if response == "Enter your password: ":
            self.query = "login_p {} ".format(self.peer)
            self.name = payload.decode('utf8')
            self.factory.clients[self.peer] = self.name
        print("Making response: {}".format(response))
        self.sendMessage(response.encode("utf8"), False)
        if response == "Logged in successfully!":
            self.query = ""
            self.sendMessage("Welcome back, {}.".format(self.name).encode("utf8"), False)
            loc = world.characters[self.name].location
            world.rooms[loc].add_entity(world.characters[self.name])

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
        world.rooms[world.characters[self.name].location].remove_entity(world.characters[self.name])


class MUDServerFactory(WebSocketServerFactory):

    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = {}

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients[client.peer] = client.peer

    def unregister(self, client):
        if client.peer in self.clients:
            print("unregistered client {}".format(client.peer))
            del self.clients[client.peer]
