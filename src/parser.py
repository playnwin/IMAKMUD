from src import world


def parse(protocol, text):
    texts = text.split(" ")
    if texts[0].lower() in ["look"]:
        look(protocol, texts[1:])
    elif texts[0].lower() in ["go", "walk", "to"]:
        go(protocol, texts[1:])
    elif texts[0].lower() in ["s", "say"]:
        say(protocol, texts[1:])
    elif texts[0].lower() in ["think"]:
        think(protocol, texts[1:])
    elif texts[0].lower() in ["w", "whisper"]:
        whisper(protocol, texts[1:])
    elif texts[0].lower() in ["take", "get"]:
        take(protocol, texts[1:])
    elif texts[0].lower() in ["i", "inventory"]:
        look_inventory(protocol, texts[1:])
    elif texts[0].lower() in ["stats"]:
        get_stats(protocol, texts[1:])
    elif texts[0].lower() in ["equip"]:
        equip(protocol, texts[1:])
    elif texts[0].lower() in ["unequip"]:
        unequip(protocol, texts[1:])
    elif texts[0].lower() in ["use"]:
        use_item(protocol, texts[1:])
    elif texts[0].lower() in ["help"]:
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
    world.players[protocol.name].say(text)


def think(protocol, text):
    world.players[protocol.name].think(text[0])


def whisper(protocol, text):
    world.players[text[0]].think("{} whispers to you: {}".format(world.players[protocol.name].name, " ".join(text[1:])))


def take(protocol, text):
    if text[0] in world.rooms[world.players[protocol.name].location].items:
        world.players[protocol.name].add_item(world.items[text[0]])
        world.rooms[world.players[protocol.name].location].remove_item(world.items[text[0]])
    else:
        protocol.sendMessage("I don't see that item.".encode("utf8"))


def look_inventory(protocol, text):
    if len(text) == 0:
        items = "Equipped: \n"
        for a in world.players[protocol.name].equipped.values():
            if a is not None:
                if a.slot is not "twoHand":
                    items += a.name + "\n"
                else:
                    if a.name not in items:
                        items += a.name + "\n"
        items += "You have: \n"
        for a in world.players[protocol.name].items.values():
            items += a.name + "\n"
        protocol.sendMessage(items.encode("utf8"))
    else:
        if text[0] in world.players[protocol.name].items:
            protocol.sendMessage(world.players[protocol.name].items[text[0]].desc.encode("utf8"))
        if text[0] in [x.id for x in world.players[protocol.name].equipped.values() if x is not None]:
            protocol.sendMessage(world.players[protocol.name].equipped[world.items[text[0]].slot].desc.encode("utf8"))


def use_item(protocol, text):
    if text in world.players[protocol.name].items:
        world.players[protocol.name].items[text].use(character = protocol.name)
    else:
        protocol.sendMessage("You can't use an item you don't have.".encode("utf8"))

def equip(protocol, text):
    if text[0] in world.items.keys():
        world.players[protocol.name].equip(world.items[text[0]])
    else:
        world.players[protocol.name].think("I can't equip that item.")

def unequip(protocol, text):
    if text[0] in world.items.keys():
        world.players[protocol.name].unequip(world.items[text[0]])
    else:
        world.players[protocol.name].think("I can't unequip that item.")

def get_stats(protocol, text):
    stats = "Stats:\n"
    for k, v in world.players[protocol.name].stats.items():
        stats+= str(k) + " - " + str(v) + "\n"
    protocol.sendMessage(stats.encode("utf8"))

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
