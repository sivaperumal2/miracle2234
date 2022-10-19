    

# Kanged By © @ITZ_STAR_BOY
# Owner Sambodhiraj
# All rights reserved. © Alisha © Sweety © Sweety




from SweetyMusic.core.bot import SweetyBot
from SweetyMusic.core.dir import dirr
from SweetyMusic.core.git import git
from SweetyMusic.core.userbot import Userbot
from SweetyMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = SweetyBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
