# -*- coding: utf-8 -*-

# For distribution

import os
import PyInstaller.__main__

os.system("echo:")
os.system("python --version")
os.system("echo Running builder to package python script into a single executable:\n")
os.system("echo:")

#os.system("pyinstaller serial_injector.py --onefile")

PyInstaller.__main__.run([
    'serial_injector.pyw',
    '--onefile',
    '--icon=pouring-breakfast-cereal-B9YDP3.ico'
    #'--windowed' #for building a mac app
])

# add commit info so you can view what the recent addition was
    # Is there a message field that could be added?