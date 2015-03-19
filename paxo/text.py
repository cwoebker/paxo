# -*- coding: utf-8 -*-
"""
paxo.text - text and print stuff
"""

from clint.textui import colored, puts, indent

from paxo.util import is_win


# www.github.com/kennethreitz/spark.py - this code is taken from kennethreitz
# python port of holman's original spark
# slightly altered


def spark_string(ints):
    """Returns a spark string from given iterable of ints."""
    ticks = u'▁▂▃▅▆▇'
    ints = [i for i in ints if type(i) == int]
    if len(ints) == 0:
        return ""
    step = (max(ints) / float(len(ticks) - 1)) or 1
    return u''.join(
        ticks[int(round(i / step))] if type(i) == int else u'.' for i in ints)


def title(text):
    if not is_win:
        text = colored.green(text)
    with indent(4):
        puts(text)
    puts("-" * (8 + len(text)))


def message(text):
    puts(text)


def info(text):
    if not is_win:
        text = colored.white(text)
    puts(text)


def warning(text):
    if not is_win:
        text = colored.yellow(text)
    puts(text)


def error(text):
    if not is_win:
        text = colored.red(text)
    puts(text)

