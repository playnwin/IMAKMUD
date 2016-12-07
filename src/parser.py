from src import world


def parse(protocol, text):
    texts = text.split(" ")
    if texts[0] == "look":
        look(protocol, texts[1:])
    elif texts[0] == "go":
        go(protocol, texts[1:])
    elif texts[0] == "say":
        say(protocol, text[3:])
    elif texts[0] == "take":
        take(protocol, text[5:])
    elif texts[0] == "i":
        look_inventory(protocol, text[2:])
    elif texts[0] == "use":
        use_item(protocol, text[4:])
    elif texts[0] == "help":
        disp_help(protocol, texts[1:])
    elif texts[0] == "login_u":
        login_username(protocol, texts[1:])
    elif texts[0] == "login_p":
        login_password(protocol, texts[1:])
    else:
        protocol.sendMessage("I couldn't understand that.".encode("utf8"))


def look(protocol, text):
    for x in range(0, len(text)-1):
        if text[x] in ["around", "at", "for", "room"]:
            del text[x]
    if len(text) == 0:
        protocol.sendMessage("You are in {}. {} In the room you see: {}{}".format(world.rooms[world.players[protocol.name].location].name,
                                                                                world.rooms[world.players[protocol.name].location].desc,
                                                                                world.rooms[world.players[protocol.name].location].contains.keys(),
                                                                                world.rooms[world.players[protocol.name].location].items.keys()).encode("utf8"))
    else:
        if (text[0] in world.rooms[world.players[protocol.name].location].contains.keys()) or (text[0] in world.rooms[world.players[protocol.name].location].items.keys()):
            protocol.sendMessage("You look at {}. {}".format(text[0], world.rooms[world.players[protocol.name].location].contains[text[0]].desc).encode("utf8"))
        else:
            protocol.sendMessage("You don't see {}.".format(text[0]).encode('utf8'))


def go(protocol, text):
    if text[0][0] == "N":
        if world.rooms[world.players[protocol.name].location].north != "":
            world.players[protocol.name].change_room(world.rooms[world.players[protocol.name].location].north)
            protocol.sendMessage("You go North into {}. {}".format(world.rooms[world.players[protocol.name].location].name,
                                                                  world.rooms[world.players[protocol.name].location].desc)
                                                                  .encode("utf8"))
        else:
            protocol.sendMessage("You can't go that way.".encode("utf8"))
    elif text[0][0] == "E":
        if world.rooms[world.players[protocol.name].location].east != "":
            world.players[protocol.name].change_room(world.rooms[world.players[protocol.name].location].east)
            protocol.sendMessage("You go East into {}. {}".format(world.rooms[world.players[protocol.name].location].name,
                                                                  world.rooms[world.players[protocol.name].location].desc)
                                                                  .encode("utf8"))
        else:
            protocol.sendMessage("You can't go that way.".encode("utf8"))
    elif text[0][0] == "S":
        if world.rooms[world.players[protocol.name].location].south != "":
            world.players[protocol.name].change_room(world.rooms[world.players[protocol.name].location].south)
            protocol.sendMessage("You go South into {}. {}".format(world.rooms[world.players[protocol.name].location].name,
                                                                  world.rooms[world.players[protocol.name].location].desc)
                                                                  .encode("utf8"))
        else:
            protocol.sendMessage("You can't go that way.".encode("utf8"))
    elif text[0][0] == "W":
        if world.rooms[world.players[protocol.name].location].west != "":
            world.players[protocol.name].change_room(world.rooms[world.players[protocol.name].location].west)
            protocol.sendMessage("You go West into {}. {}".format(world.rooms[world.players[protocol.name].location].name,
                                                                  world.rooms[world.players[protocol.name].location].desc)
                                                                  .encode("utf8"))
        else:
            protocol.sendMessage("You can't go that way.".encode("utf8"))
    else:
        protocol.sendMessage("I don't understand what direction that it.".encode("utf8"))


def say(protocol, text):
    world.rooms[world.players[protocol.name].location].broadcast(protocol.name, text)

def take(protocol, text):
    if text in world.rooms[world.players[protocol.name].location].items:
        world.players[protocol.name].add_item(world.items[text])
    else:
        protocol.sendMessage("I don't see that item.".encode("utf8"))

def look_inventory(protocol, text):
    if text == "":
        items = "You have: \n"
        for a in world.players[protocol.name].items.values():
            items += a.name
        protocol.sendMessage(items.encode("utf8"))
    else:
        if text in world.players[protocol.name].items:
            protocol.sendMessage((world.players[protocol.name].items[text].desc).encode("utf8"))

def use_item(protocol, text):
    if text in world.players[protocol.name].items:
        world.players[protocol.name].items[text].consume(protocol.name)

def disp_help(protocol, text):
    if len(text) == 0:
        protocol.sendMessage("Currently, you can [look] at things. There's not much to see.".encode("utf8"))


def login_username(protocol, text):
    if text[0] in world.factory.clients.values():
        protocol.sendMessage("That character is already logged in. Try another character.".encode("utf8"))
    elif text[0] not in (c for c in world.players.keys()):
        protocol.sendMessage("There is no character by that name. Try another name.".encode("utf8"))
    else:
        protocol.query = "login_p {} ".format(protocol.peer)
        protocol.name = text[0]
        protocol.factory.clients[protocol.peer] = text[0]
        print("Client {} logging into {}".format(protocol.peer, text[0]))
        protocol.sendMessage("Enter your password: ".encode("utf8"))


def login_password(protocol, text):
    name = world.factory.clients[text[0]]
    password = world.players[name].password
    if text[1] == password:
        protocol.sendMessage("Logged in successfully!".encode("utf8"))
        protocol.query = ""
        protocol.sendMessage("Welcome back, {}.".format(protocol.name).encode("utf8"), False)
        world.rooms[world.players[protocol.name].location].add_entity(world.players[protocol.name])
        world.rooms[world.players[protocol.name].location].alert_entrance(protocol.name)
    else:
        protocol.sendMessage("Incorrect password.".encode("utf8"))
