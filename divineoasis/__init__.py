#
# Divine Oasis
# by wsngamerz
# divineoasis/__init__.py
#

from divineoasis.config import Config
from divineoasis.directories import Directories
from divineoasis.divineoasis import DivineOasis
from divineoasis.logger import Logging

__version__ = "v0.0.1 ALPHA"
__author__ = "wsngamerz"

# initiate main classes
# and pass them through to each other
game_directories = Directories()
game_config = Config(game_directories)
game_logger = Logging(game_config)
main_game = DivineOasis(game_config, game_logger)
