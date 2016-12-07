from src import world

class Character:

    def __init__(self, name = "", desc = "", location = ""):
        self.name = name
        self.desc = desc
        self.location = location

    def is_player(self):
        return False

    def change_room(self, new_room):
        world.rooms[self.location].remove_entity(self)
        world.rooms[self.location].alert_exit(self.name)
        world.rooms[new_room].add_entity(self)
        world.rooms[new_room].alert_entrance(self.name)
        self.location = new_room


class Player(Character):

    def __init__(self, name = "", desc = "", password = "", location = ""):
        Character.__init__(self, name, desc, location)
        self.password = password

    def is_player(self):
        return True

    def say(self, text):
        world.rooms[self.location].say(self.name, text)