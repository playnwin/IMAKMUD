class Room:

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc
        self.contains = []

    def setName(self, name):
        self.name = name

    def setDesc(self, desc):
        self.desc = desc

    def addEntity(self, entity):
        self.contains.append(entity)

    def removeEntity(self, entity):
        self.contains.remove(entity)