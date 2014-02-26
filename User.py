import TwitchREST

class User:

    tr = None
    name = ""

    def __init__(self, twitch_rest, name):
        self.tr = twitch_rest
        self.name = name