from ErorMusic.core.bot import EROR
from ErorMusic.core.dir import dirr
from ErorMusic.core.git import git
from ErorMusic.core.userbot import Userbot
from ErorMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = EROR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
