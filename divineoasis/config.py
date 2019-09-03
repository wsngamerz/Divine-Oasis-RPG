#
# Divine Oasis
# by wsngamerz
# divineoasis/config.py
#

import json

from divineoasis.directories import Directories
from dotty_dict import dotty
from pathlib import Path



class Config:
    """
    The config class which handles all stored configuration of the game and
    handles setting and getting of options and paths
    """
    def __init__(self, directories: Directories):
        self.directories = directories
        self.config_file = self.directories.config_directory / "config.json"
        self._config = None

        self.directories.config_directory.mkdir(parents=True, exist_ok=True)
        self.directories.saves_directory.mkdir(parents=True, exist_ok=True)

        self.load_config()


    def load_config(self) -> None:
        """
        Loads configuration into memory and then closes file
        """
        # Check if file exists
        if not self.config_file.exists():
            # if not, create a new config file based upon a template file
            with open(self.config_file, "w") as new_config_file:
                # read config template data and save to new config file
                template_config = open(self.directories.assets_directory / "data" / "config.template.json", "r").readlines()
                new_config_file.writelines(template_config)
                new_config_file.close()
        
        with open(self.config_file, "r") as config_file:
            config_dict = json.loads(config_file.read())
            self._config = dotty(config_dict)
            config_file.close()
        
        # TODO: Check for outdated config file so that we are able to perform a migration


    def close_config(self) -> None:
        self.save_config()


    def reload_config(self) -> None:
        self.save_config()
        self._config = None
        self.load_config()


    def save_config(self) -> None:
        with open(self.config_file, "w") as config_file:
            config_data = json.dumps(self._config.to_dict())
            config_file.write(config_data)
            config_file.close()


    # Get Paths

    def get_base_directory(self) -> Path:
        return self.directories.base_directory


    def get_config_directory(self) -> Path:
        return self.directories.config_directory


    def get_assets_directory(self) -> Path:
        return self.directories.assets_directory


    def get_saves_directory(self) -> Path:
        return self.directories.saves_directory


    # Get Options

    def get_option(self, setting_path: str) -> str:
        final_string = self._config[setting_path]
                
        return final_string


    def get_option_int(self, setting_path: str) -> int:
        return int(self.get_option(setting_path))


    def get_option_bool(self, setting_path: str) -> bool:
        return bool(self.get_option(setting_path))


    # Set Options

    def set_option(self, setting_path: str, value: str) -> str:
        self._config[setting_path] = value

        return self.get_option(setting_path)
