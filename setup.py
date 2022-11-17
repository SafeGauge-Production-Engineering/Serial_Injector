# -*- coding: utf-8 -*-

# For distribution

import os

os.system("echo:")
os.system("py --version")
os.system("echo Running builder to package python script into a single executable:\n")
os.system("echo:")

os.system("pyinstaller serial_injector.py --onefile")