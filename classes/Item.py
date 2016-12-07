from src import world

class Item:
    def __init__(self, id="", name="", desc=""):
        self.id = id
        self.name = name
        self.desc = desc

class Consumable(Item):
    def __init__(self, id="", name="", desc="", effect=None):
        Item.__init__(self, id, name, desc)
        self.effect = effect

    def consume(self, character):
        self.effect(character)
