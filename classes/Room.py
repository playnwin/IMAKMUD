class Room:

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc
        self.contains = {}

    def add_entity(self, entity):
        self.contains[entity.name] = entity

    def remove_entity(self, entity):
        del self.contains[entity.name]
