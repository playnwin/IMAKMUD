from classes.Character import Character, Player
from classes.Item import Item, Consumable
from src import world

class Potions:
    def potionBear(character):
        world.rooms[world.players[character].location].broadcast(character, "Bears.")

    potionBearItem = Consumable("potionBear", "Bear Potion", "This potion seems brown and hairy.", potionBear)
