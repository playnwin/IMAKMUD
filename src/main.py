from server import servermain
from src import world
from classes.Character import Character, Player
from classes.Room import Room
from items.Potions import Potions
from items.Armors import Armors
from items.Weapons import Weapons

if __name__ == '__main__':
    world.players["Stefan"] = Player("Stefan", "The Main Character of this story.", "1234", "Jail Cell")
    world.players["Michael"] = Player("Michael", "Creator of StefansFace.com.", "1234", "Jail Cell")
    world.players["Colby"] = Player("Colby", "A literal god.", "1234", "Jail Cell")
    world.players["Elijah"] = Player("Elijah", "Bears, bears, bears.", "1234", "Jail Cell")
    world.players["Alex"] = Player("Alex", "Who knows?", "1234", "Jail Cell")
    world.characters["Joe"] = Character("Joe", "A generic dude.", "Jail Cell")
    world.characters["Guard Alex"] = Character("Guard Alex", "The man standing guard outside your jail cell. "
                                                             "He's asleep.")
    world.rooms["Jail Cell"] = Room("Jail Cell", "There's an open bar door leading into a stone hallway to "
                                                 "the North.")
    world.rooms["Jail Cell"].define_surroundings(north="Stone Hallway")
    world.rooms["Stone Hallway"] = Room("Stone Hallway", "You're at the end of a stone hallway, North of a door "
                                                         "to a jail cell")
    world.rooms["Stone Hallway"].define_surroundings(south="Jail Cell")
    world.rooms["Jail Cell"].add_entity(world.characters["Joe"])
    world.rooms["Stone Hallway"].add_entity(world.characters["Guard Alex"])

    world.items["potionBear"] = Potions.potionBearItem
    world.rooms["Jail Cell"].add_item(world.items["potionBear"])

    world.items["armorIronChest"] = Armors.armorIronChestItem
    world.rooms["Jail Cell"].add_item(world.items["armorIronChest"])

    world.items["armorRobeChest"] = Armors.armorRobeChestItem
    world.rooms["Jail Cell"].add_item(world.items["armorRobeChest"])

    world.items["weaponIronSword"] = Weapons.weaponIronSword
    world.rooms["Jail Cell"].add_item(world.items["weaponIronSword"])

    world.items["weaponWoodStaff"] = Weapons.weaponWoodStaff
    world.rooms["Jail Cell"].add_item(world.items["weaponWoodStaff"])
    servermain.start_server()
