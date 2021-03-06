from src import world


class Room:

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc
        self.contains = {}
        self.north = ""
        self.east = ""
        self.south = ""
        self.west = ""
        self.items = {}

    def add_entity(self, entity):
        self.contains[entity.name] = entity

    def add_item(self, item):
        self.items[item.id] = item

    def remove_entity(self, entity):
        del self.contains[entity.name]

    def remove_item(self, item):
        del self.items[item.id]

    def define_surroundings(self, north="", east="", south="", west=""):
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def broadcast(self, name, text):
        activeplayers = [x for x, y in self.contains.items() if y.is_player()]
        for key, value in world.factory.clients.items():
            if value in activeplayers:
                print("Broadcasting to {}".format(value))
                world.factory.link[key].sendMessage("{} says: {}".format(name, text).encode('utf8'))

    def alert_entrance(self, name):
        activeplayers = [x for x, y in self.contains.items() if y.is_player()]
        for key, value in world.factory.clients.items():
            if value in activeplayers and value != name:
                print("Alerting {}".format(value))
                world.factory.link[key].sendMessage("{} has entered {}.".format(name, self.name).encode('utf8'))

    def alert_exit(self, name):
        activeplayers = [x for x, y in self.contains.items() if y.is_player()]
        for key, value in world.factory.clients.items():
            if value in activeplayers and value != name:
                print("Alerting {}".format(value))
                world.factory.link[key].sendMessage("{} has left {}.".format(name, self.name).encode('utf8'))
