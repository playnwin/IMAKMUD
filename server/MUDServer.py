from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from src.parser import parse
from src import world


class MUDProtocol(WebSocketServerProtocol):
    query = ""
    loc = ""
    name = "Unauthenticated User"

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        self.factory.register(self)
        self.sendMessage("Enter your character name: ".encode("utf8"), False)
        self.query = "login_u "

    def onMessage(self, payload, isBianary):
        message = "{}".format(self.query) + payload.decode('utf8')
        print("Got message from {}: {}".format(self.name, message))
        parse(self, message)
        """
        if response[0:5] == "print":
            response = response[6:]
            print("Making response to {}: {}".format(self.name, response))
            self.sendMessage(response.encode("utf8"), False)
        if response[0:2] == "go":
            if response[3] == "N":
                if world.rooms[world.players[self.name].location].north != "":
                    dest_room = world.rooms[world.players[self.name].location].north
            elif response[3] == "E":
                if world.rooms[world.players[self.name].location].east != "":
                    dest_room = world.rooms[world.players[self.name].location].east
            elif response[3] == "S":
                if world.rooms[world.players[self.name].location].south != "":
                    dest_room = world.rooms[world.players[self.name].location].south
            elif response[3] == "W":
                if world.rooms[world.players[self.name].location].west != "":
                    dest_room = world.rooms[world.players[self.name].location].west
            else:
                self.sendMessage("You can't go that way.".encode("utf8"), False)
            world.players[self.name].change_room(dest_room)
        if response == "Enter your password: ":
            self.query = "login_p {} ".format(self.peer)
            self.name = payload.decode('utf8')
            self.factory.clients[self.peer] = self.name
            print("Client {} logging into {}".format(self.peer, self.name))
        if response == "Logged in successfully!":
            self.query = ""
            self.sendMessage("Welcome back, {}.".format(self.name).encode("utf8"), False)
            self.loc = world.players[self.name].location
            world.rooms[self.loc].add_entity(world.players[self.name])
            world.rooms[self.loc].alert_entrance(self.name)
        if response[0:3] == "say":
            world.rooms[self.loc].broadcast(self.name, response[4:])
        """

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed with {}: {}".format(self.name, reason))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)
        world.rooms[world.players[self.name].location].remove_entity(world.players[self.name])
        world.rooms[world.players[self.name].location].alert_exit(self.name)


class MUDServerFactory(WebSocketServerFactory):

    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = {}
        self.link = {}

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients[client.peer] = client.peer
            self.link[client.peer] = client

    def unregister(self, client):
        if client.peer in self.clients:
            print("unregistered client {}".format(client.peer))
            del self.clients[client.peer]
            del self.link[client.peer]
