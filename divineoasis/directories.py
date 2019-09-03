#
# Divine Oasis
# by wsngamerz
# divineoasis/directories.py
#

from appdirs import user_data_dir
from pathlib import Path



class Directories:
    def __init__(self):
        self.base_directory = Path(user_data_dir("Divine Oasis", "wsngamerz"))
        self.saves_directory = self.base_directory / "saves"
        self.config_directory = self.base_directory / "config"
        self.assets_directory = Path(__file__).resolve().parent / "assets"
