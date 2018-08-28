"""
paxo.core - the guts of it all
"""

import os

from clint.textui import colored, puts
from clint import resources

from paxo import __author__
from paxo.command import define_command, Collection
from paxo.util import args, show_error, ExitStatus, XDG_DATA_HOME
from paxo.storage import storage


class Paxo(object):
    def __init__(self, name, description, command_info, version,
                 default_action=None, dynamic_action=None, store=None):
        self.name = name
        self.description = description
        self.command_info = command_info
        self.version = version
        self.store = store

        resources.init(__author__, self.name)

        if self.store:
            # path = os.path.expanduser('~/.'+self.name)
            # if XDG_DATA_HOME:
            path = os.path.join(XDG_DATA_HOME, self.name, self.name)
            path = resources.user.read('path.ini') or path
            # TODO: make this more general
            self.store.setPath(path)
            self.store.bootstrap()

        self.default_action = default_action or self.display_info
        self.dynamic_action = dynamic_action or self.display_info

        define_command(name='help', short='h', fn=self.cmd_help,
                       usage='help <command>',
                       help='Display help for a command.')

    def go(self):
        if args.contains(('-h', '--help')):
            self.display_info(args)
            return ExitStatus.HELP
        elif args.contains(('-v', '--version')):
            puts('{0} v{1}'.format(
                colored.yellow(self.name),
                self.version
            ))
            return ExitStatus.VERSION
        with storage(self.store):
            arg = args.get(0)
            if arg:
                command = Collection.lookup_command(arg)
                if command:
                    self.execute(command)
                else:
                    self.dynamic_action(args)
            else:
                self.default_action(args)
        return ExitStatus.OK # ExitStatus is defined centrally and has to be adjusted at any point

    @staticmethod
    def execute(command):
        arg = args.get(0)
        args.remove(arg)
        command.__call__(args)

    def display_info(self, args):
        puts('{0} - {1}'.format(colored.yellow(self.name), self.description))
        header_info = 'Usage: {0} {1}'.format(
            colored.yellow(self.name),
            colored.green(self.command_info)
        )
        puts(header_info)
        puts('-' * len(header_info))
        for command in Collection.list_commands():
            usage = command.usage or command.name
            text = command.help or ''
            puts('{0:45} {1}'.format(colored.green(usage), text))

    def cmd_help(self, args):
        command = args.get(0)
        if command is None:
            self.display_info()
            return
        elif not Collection.lookup_command(command):
            command = 'help'
            show_error(colored.red('Unknown command: {0}'.format(args.get(0))))
        cmd = Collection.lookup_command(command)
        usage = cmd.usage or ''
        help = cmd.help or ''
        help_text = '%s - %s' % (usage, help)
        puts(help_text)
