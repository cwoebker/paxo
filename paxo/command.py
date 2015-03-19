"""
paxo.command - cli done the right way
"""

class Collection(object):
    COMMANDS = []

    @classmethod
    def clear_commands(cls):
        cls.COMMANDS = []

    @classmethod
    def list_commands(cls):
        return sorted(cls.COMMANDS,
                      key=lambda c: c.name)

    @classmethod
    def lookup_command(cls, name):
        for command in cls.COMMANDS:
            if command.name == name:
                return command
        else:
            return None

    @classmethod
    def register_command(cls, command):
        if cls.lookup_command(command.name):
            return False
        cls.COMMANDS.append(command)
        return True


class Command(object):
    def __init__(self, name=None, short=None, fn=None, usage=None, help=None):
        self.name = name
        self.short = short
        self.fn = fn
        self.usage = usage
        self.help = help

    def __call__(self, *args, **kw_args):
        return self.fn(*args, **kw_args)


def define_command(fn, name=None, short=None, usage=None, help=None):
    if not name:
        name = str(fn.func_name).replace("cmd_", "", 1)
    if not short:
        short = name
    if not usage:
        usage = name
    command = Command(name=name, short=short, fn=fn, usage=usage, help=help)
    Collection.register_command(command)
    return command


def cmd(name=None, short=None, usage=None, help=None):
    def define(fn):
        define_command(fn, name=name, short=short, usage=usage, help=help)
        return fn
    return define
