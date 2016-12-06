from server import servermain
from src import world
from classes.Character import Character
from classes.Room import Room

if __name__ == '__main__':
    world.characters.append(Character("Joe", "A generic dude"))
    world.rooms.append(Room("Jail Cell", "There's no way our"))
    servermain.startServer()