import sys
from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
from server.MUDServer import MUDProtocol, MUDServerFactory
from src import world


def start_server():
    log.startLogging(sys.stdout)
    world.factory = MUDServerFactory(u"ws://127.0.0.1:9000")
    world.factory.protocol = MUDProtocol
    reactor.listenTCP(9000, world.factory)
    reactor.run()