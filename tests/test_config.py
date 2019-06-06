#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: test_config.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

# Testing config.py

import os

from divineoasis.config import Config
from tests import utils

test_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
config = Config(test_directory)


def test_application_root_set():
    assert config.application_root == test_directory


def test_data_directory_set():
    test_data_directory = os.path.join(test_directory, "data")
    assert config.data_directory == test_data_directory


def test_config_location_set():
    test_config_location = os.path.join(test_directory, "data", "config.json")
    assert config.config_location == test_config_location


def test_config_already_exists():
    # Remove existing files if any
    utils.clear_temp()

    # Create directory for config
    temp_config_file = os.path.join(test_directory, "data")
    os.makedirs(temp_config_file)

    # Create dummy config file
    with open(os.path.join(temp_config_file, "config.json"), "w") as temp_config_file:
        temp_config_file.write("{ \"lang\":\"en\" }")
        temp_config_file.close()
    
    # Check if returns True
    assert config._locate() == True

def test_config_not_exists():
    # Remove existing files if any
    utils.clear_temp()

    # Create folder for template file
    temp_assets_dir = os.path.join(test_directory, "divineoasis", "assets")
    os.makedirs(temp_assets_dir)

    # Create template file
    with open(os.path.join(temp_assets_dir, "config.default.json"), "w") as template_file:
        template_file.write("Success")
        template_file.close()

    # Check if false
    assert config._locate()


def test_config_template_not_exists():
    # Remove existing files if any
    utils.clear_temp()

    # Check if false
    assert config._locate() == False
