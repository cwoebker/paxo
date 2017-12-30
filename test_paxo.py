#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Paxo."""

import unittest

from clint import arguments

from paxo.core import Paxo
from paxo.command import Command, cmd, define_command, Collection
from paxo.util import ExitStatus, is_win, is_lin, is_osx, args


class AbstractTestCase(unittest.TestCase):
    pass


class GeneralTestCase(AbstractTestCase):
    """Important things that shouldn't change across versions"""

    def test_exit_status(self):
        self.assertEqual(ExitStatus.OK, 0)
        self.assertEqual(ExitStatus.ERROR, 1)
        self.assertEqual(ExitStatus.ABORT, 2)
        self.assertEqual(ExitStatus.HELP, 3)
        self.assertEqual(ExitStatus.VERSION, 4)
        self.assertEqual(ExitStatus.UNSUPPORTED, 5)

    def test_operating_system(self):
        def fn(c):
            if c:
                return 1
            return 0
        self.assertTrue(sum(map(fn, [is_win, is_lin, is_osx])) <= 1)

    def test_arguments(self):
        self.assertTrue(isinstance(args, arguments.Args))


class PaxoTestCase(AbstractTestCase):
    """Paxo test cases."""

    def setUp(self):
        self.paxo = Paxo('paxo', 'a test paxo', '<do this>', '0.1')

    def tearDown(self):
        """Teardown."""
        del self.paxo

    def test_init(self):
        self.assertEqual(self.paxo.name, 'paxo')
        self.assertEqual(self.paxo.description, 'a test paxo')
        self.assertEqual(self.paxo.command_info, '<do this>')
        self.assertEqual(self.paxo.version, '0.1')
        # self.assertEqual(self.paxo.__class__, '') # verify this later with Juan

    def test_info(self):
        pass

    def test_help(self):
        pass


class CommandTestCase(AbstractTestCase):
    def tearDown(self):
        Collection.clear_commands()

    def test_define_command(self):
        ret = define_command(name='test', fn=len, usage='test (<test_arg>)',
                             help='testing stuff')
        self.assertTrue(isinstance(ret, Command))
        self.assertEqual(len(Collection.list_commands()), 1)


class CommandManagerTestCase(AbstractTestCase):
    def setUp(self):
        self.testCommand = define_command(name='test', fn=len, usage='test (<test_arg>)',
                             help='testing stuff')

    def tearDown(self):
        Collection.clear_commands()

    def test_cmd_decorator_command(self):
        @cmd()
        def hello(args):
            print 'Hello World!'
        self.assertEqual(hello, Collection.lookup_command('hello').fn)

    def test_list_commands(self):
        self.assertEqual(len(Collection.list_commands()), len(Collection.COMMANDS))
        self.assertEqual(len(Collection.list_commands()), 1)

    def test_lookup_command(self):
        self.assertTrue(isinstance(Collection.lookup_command('test'), Command))
        self.assertEqual(Collection.lookup_command('test'), self.testCommand)

    def test_register_command(self):
        test = Command(name='test1', short=None, fn=len,
                       usage='test1 hi', help="testing stuff 1")
        Collection.register_command(test)
        self.assertEqual(test, Collection.lookup_command('test1'))

    def test_double_command(self):
        test = Command(name='test', short=None, fn=len,
                       usage='test1 hi', help="testing stuff 1")
        self.assertFalse(Collection.register_command(test))


class CrossPlatformTestCase(AbstractTestCase):
    pass


class ExecuteTestCase(AbstractTestCase):

    def setUp(self):
        self.paxo = Paxo('paxo', 'a test paxo', '<do this>', '0.1')

    def tearDown(self):
        del self.paxo


class TextTestCase(AbstractTestCase):
    pass


class StorageTestCase(AbstractTestCase):
    pass


class AutoStartTestCase(AbstractTestCase):
    pass

if __name__ == '__main__':
    unittest.main()
