from typing import Type
from quart import Quart
# Import all route blueprints
from routes.achievements import Achievements
from routes.dev import Dev
from routes.friends import Friends
from routes.presence import Presence
from routes.profile import Profile
from routes.usercolors import Usercolors
from routes.userstats import Userstats
from routes.xuid import Xuid

class Routes:
    def __init__(self, app: Quart, loop, xbl_client, cache):
        self.app = app
        self.loop = loop
        self.xbl_client = xbl_client
        self.cache = cache

        self.register_batch([
            Achievements,
            Dev,
            Friends,
            Presence,
            Profile,
            Usercolors,
            Userstats,
            Xuid
        ])
    
    def register(self, cls: Type):
        self.app.register_blueprint(cls(self.loop, self.xbl_client, self.cache).app, url_prefix="/%s" % cls.__name__.lower())
    
    def register_batch(self, dict: dict[Type]):
        for cls in dict:
            self.register(cls)
