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

    def use(self, character):
        self.consume(character)

    def consume(self, character):
        self.effect(character)
        del world.players[character].items[self.id]

"""
Elijah's Code
class Equippable(Item):
    def __init__(self, id="", name="", desc="", slot=None,equip=None, unequip=None):
        Item.__init__(self, id, name, desc)
        self.onEquip = equip
        self.onUnequip = unequip
        self.slot = slot

class Armor(Equippable):
    def __init__(self, id="", name="", desc="", slot=None,equip=None, unequip=None, statChange={}, onHitEffect=None):
        Equippable.__init__(self, id, name, desc, slot, equip, unequip)
        self.statChange = statChange
        self.onHitEffect = onHitEffect

class Weapon(Equippable):
    def __init__(self, id="", name="", desc="", slot=None, equip=None, unequip=None, statChange={}, onHitEffect=None):
        Equippable.__init__(self, id, name, desc, slot, equip, unequip)
        self.statChange = statChange
        self.onHitEffect = onHitEffect

"""
class Equippable(Item):
    def __init__(self, id="", name="", desc="", slot=None):
        Item.__init__(self, id, name, desc)
        self.slot = slot


class Armor(Equippable):
    def __init__(self, id="", name="", desc="", slot=None, damage_reduction=0, agility_reduction=0, armor_type=""):
        Equippable.__init__(self, id, name, desc, slot)
        self.damage_reduction = damage_reduction
        self.agility_reduction = agility_reduction
        self.armor_type = armor_type

    def on_equip(self):
        pass

class Weapon(Equippable):
    def __init__(self, id="", name="", desc="", slot=None, damage=0, weapon_type="", accuracy=0):
        Equippable.__init__(self, id, name, desc, slot)
        self.damage = damage
        self.weapon_type = weapon_type
        self.accuracy = accuracy

    def on_equip(self):
        pass
