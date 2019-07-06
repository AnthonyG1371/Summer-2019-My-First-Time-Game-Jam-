init python:
    class main_stats:
        def __init__(self, friendship, morals, pride):
            self.friendship = friendship
            self.morals = morals
            self.pride = pride
        def get_friendship(self):
            return self.friendship
        def set_friendship(self, value):
            self.friendship = value
        def get_morals(self):
            return self.morals
