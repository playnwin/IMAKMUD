from src import world


class Item:
    def __init__(self, id="", name="", desc=""):
        self.id = id
        self.name = name
        self.desc = desc

    def use(self, **kwargs):
        if type(self) is Consumable:
            self.consume(**kwargs)


class Consumable(Item):
    def __init__(self, id="", name="", desc="", effect=None):
        Item.__init__(self, id, name, desc)
        self.effect = effect

    def consume(self, **kwargs):
        self.effect(kwargs.get('character'))
        del world.players[kwargs.get('character')].items[self.id]


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
