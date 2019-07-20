init python:
    class main_stats:
        def __init__(self):
            self.friendship = 0
            self.morals = 0
        def get_friendship(self):
            return int(friendship)
        def add_friendship(self, value):
            self.friendship += value
        def get_morals(self):
            return int(self.morals)
        def add_morals(self, value):
            self.morals += value
        def add_both(self, value):
            self.friendship += value
            self.morals += value
        def set_both(self, value):
            self.friendship = value
            self.morals = value
