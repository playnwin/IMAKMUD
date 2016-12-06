class Character:
    name = ""
    desc = ""

    def __init__(self, name = None, desc = None):
        self.name = name
        self.desc = desc

    def setName(self, name):
        self.name = name

    def setDesc(self, desc):
        self.desc = desc