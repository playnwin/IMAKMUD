from src import world
from classes.Item import Item, Equippable, Armor, Weapon


class Character:
    def __init__(self, name="", desc="", location=""):
        self.name = name
        self.desc = desc
        self.location = location
        self.items = {}
        self.equipped = {'head': None, 'neck': None, 'chest': None, 'back': None, 'hands': None,
                         'legs': None, 'feet': None, 'ring1': None, 'ring2': None, 'misc1': None, 'misc2': None,
                         'misc3': None, 'mainHand': None, 'offHand': None}
        self.unmodifiedstats = {'dr' : 0, 'hp' : 100}
        self.stats = {'dr' : 0, 'hp' : 100}

    def is_player(self):
        return False

    def change_room(self, new_room):
        world.rooms[self.location].remove_entity(self)
        world.rooms[self.location].alert_exit(self.name)
        world.rooms[new_room].add_entity(self)
        world.rooms[new_room].alert_entrance(self.name)
        self.location = new_room

    def add_item(self, item):
        self.items[item.id] = item

    def say(self, text):
        world.rooms[self.location].broadcast(self.name, text)

    def update_stats(self):
        self.stats = dict(self.unmodifiedstats)
        for a in self.equipped.values():
            if a is not None:
                for b in a.statChange.keys():
                    self.stats[b] += a.statChange[b]

    def equip(self, item):
        if item.id in self.items.keys():
            if self.equipped[item.slot] is None:
                if item.onEquip is not None:
                    item.onEquip(self)
                self.equipped[item.slot] = item
                del self.items[item.id]
                self.update_stats()
            else:
                if type(self) is Player:
                    self.think("I'm already wearing something there.")
        else:
            if type(self) is Player:
                self.think("I can't equip something I don't have.")

    def unequip(self, item):
        if self.equipped[item.slot].id is item.id:
            if item.onUnequip is not None:
                item.onUnequip(self)
            self.items[item.id] = item
            self.equipped[item.slot] = None
            self.update_stats()
        else:
            if type(self) is Player:
                self.think("I'm not wearing that item.")

class Player(Character):
    def __init__(self, name="", desc="", password="", location=""):
        Character.__init__(self, name, desc, location)
        self.password = password

    def is_player(self):
        return True

    def think(self, text):
        print("Telling {}, {}".format(self.name, text))
        for k,v in world.factory.clients.items():
            if self.name == v:
                world.factory.link[k].sendMessage(text.encode("utf8"))