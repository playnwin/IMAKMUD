from classes.Item import Item, Equippable, Weapon

class Weapons:

    weaponIronSword = Weapon("weaponIronSword", "Iron Sword", "This sword seems reliable.", slot="oneHand", statChange={'accuracy' : 10})
    weaponWoodStaff = Weapon("weaponWoodStaff", "Wooden Staff", "This staff is gnarled and burnt.", slot="twoHand", statChange={'accuracy':-10})