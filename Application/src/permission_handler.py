import os
import platform
import ctypes
import sys
import subprocess

def is_admin(platform):
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False