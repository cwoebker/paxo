#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import json
import zlib
from collections import OrderedDict
from contextlib import contextmanager

@contextmanager
def storage(store=None):
    if store:
        store.read()
    yield
    if store:
        store.save()


class AbstractStorage(object):
    def __init__(self):
        pass


class SimpleStorage(AbstractStorage):
    """Data is stored in a dictionary by default. This can be easily replaced though. The data just has to be stored in
    self.data"""
    def __init__(self, path=None):
        self.data = {}
        self.path = path

    def __write__(self):
        open(self.path, 'w').write(zlib.compress(json.dumps(self.data)))

    def bootstrap(self):
        if not os.path.exists(self.path):
            self.__write__()
        else:
            with open(self.path, 'r') as store:
                path = json.loads(
                    zlib.decompress(store.read()),
                    object_pairs_hook=OrderedDict).get("__PATH__")
                if path:
                    self.path = path
                    self.__write__()

    def setPath(self, path):
        if not self.path:
            self.path = path

    def read(self):
        with open(self.path, 'r') as store:
            self.data = json.loads(zlib.decompress(store.read()),
                                   object_pairs_hook=OrderedDict)

    def save(self):
        with open(self.path, 'w') as store:
            store.write(zlib.compress(json.dumps(self.data)))
