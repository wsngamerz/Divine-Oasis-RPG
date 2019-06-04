#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: divineoasis.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

from divineoasis.assets import Assets
from divineoasis.config import Config


class DivineOasis:
    def __init__(self):
        self.config = Config()
        self.assets = Assets()

    def start(self):
        print("Starting Divine Oasis")
