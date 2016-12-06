from src import world


def parse(text):
    text = text.split(" ")
    if text[0] == "look":
        return look(text[1:])
    elif text[0] == "help":
        return disp_help(text[1:])
    elif text[0] == "login":
        return login(text[1:])
    return "I couldn't understand that."


def look(text):
    if len(text) == 0:
        return "You are in {}. {}".format(world.rooms[0].name, world.rooms[0].desc)
    elif text[0] == "around":
        return "You are in {}. {}".format(world.rooms[0].name, world.rooms[0].desc)
    elif text[0] == "at":
        if text[1] in (c.name for c in world.characters):
            x = 0
            for y in range(1, len(world.characters)):
                if text[1] == world.characters[y].name:
                    x = y
                    break
            return "You look at {}. {}".format(world.characters[x].name, world.characters[x].desc)


def disp_help(text):
    if len(text) == 0:
        return "Currently, you can [look around] or you can [look at] something. Probably Joe. " \
               "Nothing else has been added."


def login(text):
    if text[0] in (c.name for c in world.characters):
        x = 0
        for y in range(1, len(world.characters)):
            if text[0] == world.characters[y].name:
                x = y
                break
        if text[1] == world.characters[x].password:
            return "Login successful. Welcome back, {}".format(world.characters[x].name)
        else:
            return "Login unsuccessful. Have a nice day."
    else:
        return "I couldn't find a character by that name."