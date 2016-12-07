from classes.Item import Item, Equippable, Armor
from src import world

class Armors:

    armorIronChestItem = Armor("armorIronChest", "Iron Chestplate", "This chestplate is heavy and sturdy.", slot='chest', statChange={'dr' : 3, 'hp' : -30})
    armorRobeChestItem = Armor("armorRobeChest", "Brown Robe", "This patchy robe is wafer-thin.", slot='chest', statChange={'dr' : -3, 'hp' : 30})