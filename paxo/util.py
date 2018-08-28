# -*- coding: utf-8 -*-
"""
paxo.util - various stuff that helps
"""

import os
import sys
import platform

from clint import arguments

__all__ = [
    'XDG_CACHE_HOME', 'XDG_CONFIG_DIRS', 'XDG_CONFIG_HOME', 'XDG_DATA_DIRS',
    'XDG_DATA_HOME', 'XDG_RUNTIME_DIR'
]

system = platform.system().lower()

is_osx = (system == 'darwin')
is_win = (system == 'windows')
is_lin = (system == 'linux')

args = arguments.Args()

DEBUG_MODE = False
if args.contains(('-d', '--dev')):
    DEBUG_MODE = True


class ExitStatus:
    """Exit status code constants."""
    OK = 0
    ERROR = 1
    ABORT = 2
    HELP = 3
    VERSION = 4
    UNSUPPORTED = 5


def show_error(msg):
    sys.stdout.flush()
    sys.stderr.write(msg + '\n')


XDG_CACHE_HOME = os.environ.get('XDG_CACHE_HOME') or os.path.expandvars(os.path.join("$HOME", ".cache"))
XDG_CONFIG_DIRS = os.environ.get('XDG_CONFIG_DIRS')
XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME') or os.path.expandvars(os.path.join("$HOME", ".config"))
XDG_DATA_DIRS = os.environ.get('XDG_DATA_DIRS')
XDG_DATA_HOME = os.environ.get('XDG_DATA_HOME') or os.path.expandvars(os.path.join("$HOME", ".local", "share"))
XDG_RUNTIME_DIR = os.environ.get('XDG_RUNTIME_DIR')
