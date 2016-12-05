import sys
from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
from server import MUDProtocol

def startServer():
    log.startLogging(sys.stdout)
    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MUDProtocol
    reactor.listenTCP(9000, factory)
    reactor.run()