from src import world


class Room:

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc
        self.contains = {}

    def add_entity(self, entity):
        self.contains[entity.name] = entity

    def remove_entity(self, entity):
        del self.contains[entity.name]

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