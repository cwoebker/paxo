#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import paxo
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Grab requirments.
with open('reqs.txt') as f:
    required = f.readlines()
settings = dict()

settings.update(
    name=paxo.__title__,
    version=paxo.__version__,
    description='paxo: python ♡ terminal',
    long_description=(open('README.md').read()),
    author=paxo.__author__,
    author_email='me@cwoebker.com',
    url='https://github.com/cwoebker/paxo',
    license=paxo.__license__,
    install_requires=required,
    tests_require=['nose'],
    packages=[
        'paxo',
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Topic :: Text Processing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ),
)

setup(**settings)
