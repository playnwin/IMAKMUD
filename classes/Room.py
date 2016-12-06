class Room:

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc
        self.contains = []

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc

    def add_entity(self, entity):
        self.contains.append(entity)

    def remove_entity(self, entity):
        self.contains.remove(entity)