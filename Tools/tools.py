import os
import sys



def to_absolute(relative_path):
    return os.path.abspath(os.path.join(find_base_dir(), relative_path))


def find_base_dir():
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller bundles put resources in _MEIPASS
        return os.path.join(sys._MEIPASS, 'Resources')
    else:
        # Use the script's actual folder to resolve ../pkgs
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.abspath(os.path.join(script_dir, "../pkgs"))

