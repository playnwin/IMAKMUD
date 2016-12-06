from src import world


def parse(text):
    text = text.split(" ")
    if text[0] == "look":
        if text[1] == "around":
            return "You are in {}. {}".format(world.rooms[0].name, world.rooms[0].desc)
        elif text[1] == "at":
            if text[2] in (c.name for c in world.characters):
                x = 0
                for x in range(1,len(world.characters)):
                    if text[2] == world.characters[x].name:
                        break
                return "You look at {}. {}".format(world.characters[x].name, world.characters[x].desc)
    elif text[0] == "help":
        return "Currently, you can [look around] or you can [look at] something. Probably Joe. Nothing else has been added."
    return "I couldn't understand that"