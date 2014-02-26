import TwitchREST


class Channel:

    name = ""

    def __init__(self, name):
        self.name = name

    def get_followers(self):
        return TwitchREST.get("channels/" + self.name + "/follows" + "?order=DESC")['follows']