#!/usr/bin/python3
"""
Write a Python program to get the Python version you are using
"""

import os
cmd = 'echo "Python Version: $(/usr/bin/python3 -V)"'
os.system(cmd)