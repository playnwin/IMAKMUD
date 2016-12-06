from src import world

class Character:

    def __init__(self, name = "", desc = "", location = ""):
        self.name = name
        self.desc = desc
        self.location = location

    def is_player(self):
        return False


class Player(Character):

    def __init__(self, name = "", desc = "", password = "", location = ""):
        Character.__init__(self, name, desc, location)
        self.password = password

    def is_player(self):
        return True

    def say(self, text):
        world.rooms[self.location].say(self.name, text)