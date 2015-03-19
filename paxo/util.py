# -*- coding: utf-8 -*-
"""
paxo.util - various stuff that helps
"""

import sys
import platform

from clint import arguments


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
