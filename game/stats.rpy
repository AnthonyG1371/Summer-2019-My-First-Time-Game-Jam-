init python:
    class main_stats:
        def __init__(self, friendship, morals, pride):
            self.friendship = friendship
            self.morals = morals
            self.pride = pride
        def get_friendship(self):
            return self.friendship
        def add_friendship(self, value):
            self.friendship += value
        def get_morals(self):
            return self.morals
        def add_morals(self, value):
            self.morals += value
        def add_both(self, value):
            self.friendship += value
            self.morals += value
