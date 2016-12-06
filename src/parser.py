from src import world


def parse(text):
    text = text.split(" ")
    if text[0] == "look":
        return look(text[1:])
    elif text[0] == "help":
        return disp_help(text[1:])
    elif text[0] == "login_u":
        return login_username(text[1:])
    elif text[0] == "login_p":
        return login_password(text[1:])
    return "I couldn't understand that."


def look(text):
    if len(text) == 0:
        return "You are in {}. {}".format(world.rooms["Jail Cell"].name, world.rooms["Jail Cell"].desc)
        print(world.rooms["Jail Cell"])
    elif text[0] == "around":
        return "You are in {}. {}".format(world.rooms["Jail Cell"].name, world.rooms["Jail Cell"].desc)
    elif text[0] == "at":
        print(world.rooms["Jail Cell"].contains)
        if text[1] in world.rooms["Jail Cell"].contains.keys():
            return "You look at {}. {}".format(text[1], world.characters[text[1]].desc)


def disp_help(text):
    if len(text) == 0:
        return "Currently, you can [look around] or you can [look at] something. Probably Joe. " \
               "Nothing else has been added."


def login_username(text):
    if text[0] in world.factory.clients.values():
        return "That character is already logged in. Try another character."
    elif text[0] not in (c for c in world.characters.keys()):
        return "There is no character by that name. Try another name."
    else:
        return "Enter your password: "


def login_password(text):
    name = world.factory.clients[text[0]]
    password = world.characters[name].password
    if text[1] == password:
        return "Logged in successfully!"
    else:
        return "Incorrect password."










    """
    if text[0] in (c.name for c in world.characters):
        x = 0
        for y in range(1, len(world.characters)):
            if text[0] == world.characters[y].name:
                x = y
                break
        if text[1] == world.characters[x].password:
            return "Login successful. Welcome back, {}.".format(world.characters[x].name)
        else:
            return "Login unsuccessful. Have a nice day."
    else:
        return "I couldn't find a character by that name."
    """