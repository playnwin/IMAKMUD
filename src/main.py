from server import servermain
from src import world
from classes.Character import Character, Player
from classes.Room import Room

if __name__ == '__main__':
    world.players["Stefan"] = Player("Stefan", "The Main Character of this story.", "1234", "Jail Cell")
    world.players["Michael"] = Player("Michael", "Stefan's Sidekick.", "1234", "Jail Cell")
    world.players["Colby"] = Player("Colby", "A literal god.", "1234", "Jail Cell")
    world.players["Elijah"] = Player("Elijah", "Bears, bears, bears.", "1234", "Jail Cell")
    world.players["Alex"] = Player("Alex", "Who knows?", "1234", "Jail Cell")
    world.characters["Joe"] = Character("Joe", "A generic dude.", "Jail Cell")
    world.rooms["Jail Cell"] = Room("Jail Cell", "There's no way out.")
    world.rooms["Jail Cell"].add_entity(world.characters["Joe"])
    servermain.start_server()
