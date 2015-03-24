#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
paxo example.py file

__author__ = 'cwoebker'
__license__ = 'MIT'
__copyright__ = '(c) 2015 Cecil Woebker'
"""

from paxo.core import Paxo
from paxo.command import cmd


@cmd(help='Print out a help message.')
def hello(args):
    print 'Hello World!'

app = Paxo('example', 'a Cecil Woebker project.', '<command>', '0.1')

if __name__ == '__main__':
    app.go()
