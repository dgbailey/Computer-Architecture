#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
filepath = sys.argv[1]
cpu = CPU()

cpu.load(filepath)
cpu.run()