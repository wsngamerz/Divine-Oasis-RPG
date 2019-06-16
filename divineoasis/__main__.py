#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: __main__.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import sys

from divineoasis.game import DivineOasis

debug_mode = False

if len(sys.argv) > 1:
    arguments = sys.argv
    arguments.pop(0)

    if "debug" in arguments:
        debug_mode = True

divineOasis = DivineOasis(debug=debug_mode)
divineOasis.start()
