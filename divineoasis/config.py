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

        # ensure that the folders exist before attempting to read from them
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
        
        # now open the actual config file
        with open(self.config_file, "r") as config_file:
            config_dict = json.loads(config_file.read())
            self._config = dotty(config_dict)
            config_file.close()
        
        # TODO: Check for outdated config file so that we are able to perform a migration


    def close_config(self) -> None:
        """
        Performs actions upon the config file (usually) when the game closes
        """
        self.save_config()


    def reload_config(self) -> None:
        """
        Re-syncs the contents of the config in-memory to the config stored on disk
        """
        self.save_config()
        self._config = None
        self.load_config()


    def save_config(self) -> None:
        """
        Writes the contents of the config in-memory to the disk
        """
        with open(self.config_file, "w") as config_file:
            config_data = json.dumps(self._config.to_dict())
            config_file.write(config_data)
            config_file.close()


    # Get Paths

    def get_base_directory(self) -> Path:
        """
        Returns the base directory path of the game which is usually located in user storage.

        Base directory refers to user storage, not where the game is stored
        """
        return self.directories.base_directory


    def get_config_directory(self) -> Path:
        """
        Returns the config directory path
        """
        return self.directories.config_directory


    def get_assets_directory(self) -> Path:
        """
        Returns the assets directory path
        """
        return self.directories.assets_directory


    def get_saves_directory(self) -> Path:
        """
        Returns the save directory path
        """
        return self.directories.saves_directory


    # Get Options

    def get_option(self, setting_path: str) -> str:
        """
        Gets a config option based upon a settings path which is usually
        a dot path and returns the value as a string
        """
        final_string = self._config[setting_path]
                
        return final_string


    def get_option_int(self, setting_path: str) -> int:
        """
        Does the exact same as get_option except casts the return type to
        an integer
        """
        return int(self.get_option(setting_path))


    def get_option_bool(self, setting_path: str) -> bool:
        """
        Does the exact same as get_option except casts the return type to
        a boolean
        """
        return bool(self.get_option(setting_path))


    # Set Options

    def set_option(self, setting_path: str, value: str) -> str:
        """
        Sets a value in config based upon a settings path which is usually
        a dot path then returns the value set from the config
        """
        self._config[setting_path] = value

        return self.get_option(setting_path)
