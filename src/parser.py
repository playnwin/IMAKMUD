from src import world


def parse(text):
    texts = text.split(" ")
    if texts[0] == "look":
        return look(texts[1:])
    elif texts[0] == "say":
        return text
    elif texts[0] == "help":
        return disp_help(texts[1:])
    elif texts[0] == "login_u":
        return login_username(texts[1:])
    elif texts[0] == "login_p":
        return login_password(texts[1:])
    return "I couldn't understand that."


def look(text):
    for x in range(0, len(text)-1):
        if text[x] in ["around", "at", "for", "room"]:
            del text[x]
    if len(text) == 0:
        return "You are in {}. {} In the room you see: {}".format(world.rooms["Jail Cell"].name,
                                                              world.rooms["Jail Cell"].desc,
                                                              world.rooms["Jail Cell"].contains.keys())
    else:
        if text[0] in world.rooms["Jail Cell"].contains.keys():
            return "You look at {}. {}".format(text[0], world.rooms["Jail Cell"].contains[text[0]].desc)
        else:
            return "You don't see {}.".format(text[0])


def disp_help(text):
    if len(text) == 0:
        return "Currently, you can look at things. There's not much to see."


def login_username(text):
    if text[0] in world.factory.clients.values():
        return "That character is already logged in. Try another character."
    elif text[0] not in (c for c in world.players.keys()):
        return "There is no character by that name. Try another name."
    else:
        return "Enter your password: "


def login_password(text):
    name = world.factory.clients[text[0]]
    password = world.players[name].password
    if text[1] == password:
        return "Logged in successfully!"
    else:
        return "Incorrect password."
