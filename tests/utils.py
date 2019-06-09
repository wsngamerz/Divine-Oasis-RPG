#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: utils.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import os
import shutil

# Clear Temp Folder

def clear_temp():
    try:
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        containing_dirs = ["data", "divineoasis"]

        for directory in containing_dirs:
            shutil.rmtree(os.path.join(temp_dir, directory))

    except FileNotFoundError:
        pass
