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
        with open(self.path, 'wb') as store:
            store.write(zlib.compress(json.dumps(self.data).encode('utf-8')))

    def bootstrap(self):
        if not os.path.exists(self.path):
            self.__write__()
        else:
            with open(self.path, 'rb') as store:
                tmp = zlib.decompress(store.read())
                jsontmp = json.loads(tmp, object_pairs_hook=OrderedDict)
                path = jsontmp.get("__PATH__")
                if path:
                    self.path = path
                    self.__write__()

    def setPath(self, path):
        if not self.path:
            self.path = path

    def read(self):
        with open(self.path, 'rb') as store:
            self.data = json.loads(zlib.decompress(store.read()), object_pairs_hook=OrderedDict)

    def save(self):
        with open(self.path, 'wb') as store:
            store.write(zlib.compress(json.dumps(self.data).encode('utf-8')))
