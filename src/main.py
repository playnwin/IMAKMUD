from server import servermain
from src import world
from classes.Character import Character
from classes.Room import Room

if __name__ == '__main__':
    world.characters["Stefan"] = Character("Stefan", "The Main Character of this story", "1234", "Jail Cell")
    world.characters["Joe"] = Character("Joe", "A generic dude.", "1234", "Jail Cell")
    world.rooms["Jail Cell"] = Room("Jail Cell", "There's no way out.")
    servermain.start_server()
