class Character:

    def __init__(self, name = None, desc = None, password=None):
        self.name = name
        self.desc = desc
        self.password = password

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc

    def set_password(self, password):
        self.password = password