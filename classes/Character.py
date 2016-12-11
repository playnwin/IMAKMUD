from src import world
from classes.Item import Item, Equippable, Armor, Weapon


class Character:
    def __init__(self, name="", desc="", location=""):
        self.name = name
        self.desc = desc
        self.location = location
        self.stats = {"health": 100, "accuracy": 0, "damage": 50, "weapon_type": "piercing",
                      "damage_reduction": 10, "armor_type": "chain"}

    def is_player(self):
        return False
"""
Elijah's Code
    def update_stats(self):
        self.stats = dict(self.unmodifiedstats)
        for a in self.equipped.values():
            if a is not None:
                if type(a) is Armor:
                    for b in a.statChange.keys():
                        self.stats[b] += a.statChange[b]
                elif type(a) is Weapon:
                    if a.slot == "oneHand":
                        for b in a.statChange.keys():
                            self.stats[b] += a.statChange[b]
                    elif a.slot == "twoHand":
                        for b in a.statChange.keys():
                            self.stats[b] += (a.statChange[b] // 2)

    def equip(self, item):
        if type(item) is Armor:
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
        elif type(item) is Weapon:
            if item.id in self.items.keys():
                if item.slot=="oneHand":
                    if self.equipped['mainHand'] is None:
                        if item.onEquip is not None:
                            item.onEquip(self)
                        self.equipped['mainHand'] = item
                        del self.items[item.id]
                        self.update_stats()
                    elif self.equipped['offHand'] is None:
                        if item.onEquip is not None:
                            item.onEquip(self)
                        self.equipped['offHand'] = item
                        del self.items[item.id]
                        self.update_stats()
                    else:
                        if type(self) is Player:
                            self.think("I'm already wearing something there.")
                elif item.slot=="twoHand":
                    if self.equipped['mainHand'] is None and self.equipped['offHand'] is None:
                        if item.onEquip is not None:
                            item.onEquip(self)
                        self.equipped['mainHand'] = item
                        self.equipped['offHand'] = item
                        del self.items[item.id]
                        self.update_stats()
                    else:
                        if type(self) is Player:
                            self.think("I'm already wearing something there.")
            else:
                if type(self) is Player:
                    self.think("I can't equip something I don't have.")

    def unequip(self, item):
        if type(item) is Armor:
            if self.equipped[item.slot].id is item.id:
                if item.onUnequip is not None:
                    item.onUnequip(self)
                self.items[item.id] = item
                self.equipped[item.slot] = None
                self.update_stats()
            else:
                if type(self) is Player:
                    self.think("I'm not wearing that item.")
        elif type(item) is Weapon:
            if item.slot == "oneHand":
                if self.equipped['offHand'] is not None and self.equipped['offHand'].id is item.id:
                    if item.onUnequip is not None:
                        item.onUnequip(self)
                    self.items[item.id] = item
                    self.equipped['offHand'] = None
                    self.update_stats()
                elif self.equipped['mainHand'].id is item.id:
                    if item.onUnequip is not None:
                        item.onUnequip(self)
                    self.items[item.id] = item
                    self.equipped['mainHand'] = None
                    self.update_stats()
            elif item.slot == "twoHand":
                if self.equipped['mainHand'].id is item.id:
                    if item.onUnequip is not None:
                        item.onUnequip(self)
                    self.items[item.id] = item
                    self.equipped['mainHand'] = None
                    self.equipped['offHand'] = None
                    self.update_stats()
"""
class Player(Character):
    def __init__(self, name="", desc="", password="", location=""):
        Character.__init__(self, name, desc, location)
        self.password = password
        self.items = {}
        self.equipped = {'head': None, 'neck': None, 'chest': None, 'back': None, 'hands': None,
                         'legs': None, 'feet': None, 'ring1': None, 'ring2': None, 'misc1': None, 'misc2': None,
                         'misc3': None, 'mainHand': None, 'offHand': None}
        self.unmodifiedstats = {'dr' : 0, 'hp' : 100, 'accuracy' : 20}
        self.stats = {'dr' : 0, 'hp' : 100, 'accuracy' : 20}

    def is_player(self):
        return True

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

    def think(self, text):
        print("Telling {}, {}".format(self.name, text))
        for k,v in world.factory.clients.items():
            if self.name == v:
                world.factory.link[k].sendMessage(text.encode("utf8"))


class Player(Character):
    def __init__(self, name="", desc="", password="", location=""):
        Character.__init__(self, name, desc, location)
        self.password = password
        self.items = []
        self.equipped = {'head': None, 'neck': None, 'chest': None, 'back': None, 'hands': None,
                         'legs': None, 'feet': None, 'ring1': None, 'ring2': None, 'misc1': None, 'misc2': None,
                         'misc3': None, 'mainHand': None, 'offHand': None}
        self.stats = {"health": 100, "mana": 100, "strength": 10, "agility": 10, "spellcasting": 10}

    def is_player(self):
        return True

    def change_room(self, new_room):
        world.rooms[self.location].remove_entity(self)
        world.rooms[self.location].alert_exit(self.name)
        world.rooms[new_room].add_entity(self)
        world.rooms[new_room].alert_entrance(self.name)
        self.location = new_room

    def add_item(self, item):
        self.items.append(item)

    def say(self, text):
        world.rooms[self.location].broadcast(self.name, text)

    def think(self, text):
        print("Telling {}, {}".format(self.name, text))
        for k,v in world.factory.clients.items():
            if self.name == v:
                world.factory.link[k].sendMessage(text.encode("utf8"))

    def equip(self, item):
        if item.slot == "twoHand" or self.equipped[item.slot] is None:
            self.think("You equipped {}.".format(item.name))
            if item.slot == "twoHand":
                self.equipped["mainHand"] = item
                self.equipped["offHand"] = item
            else:
                self.equipped[item.slot] = item
            self.items.remove(item)
        else:
            self.think("You switched {} for {}.".format(self.equipped[item.slot].name, item.name))
            self.items.append(self.equipped[item.slot])
            if self.equipped[item.slot] == "twoHand":
                self.equipped["mainHand"] = None
                self.equipped["offHand"] = None
            if item.slot == "twoHand":
                self.equipped["mainHand"] = item
                self.equipped["offHand"] = item
            else:
                self.equipped[item.slot] = item
            self.items.remove(item)

    def unequip(self, item):
        self.think("You unequipped {}.".format(item.name))
        self.items.append(item)
        if item.slot == "twoHand":
            self.equipped["mainHand"] = None
            self.equipped["offHand"] = None
        else:
            self.equipped[item.slot] = None
