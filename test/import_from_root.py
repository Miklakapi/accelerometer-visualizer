#!/usr/bin/env python

"""Adds a path for importing between directories to work"""

import sys

sys.path.insert(1, sys.path[0][0:-4])
sys.path.insert(1, sys.path[0][0:-4] + 'src')
print(sys.path)
