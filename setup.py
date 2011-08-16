#-*- coding:utf-8 -*-
#
# Copyright (C) 2011 - Brantley Harris <brantley.harris@gmail.com>
#
# Distributed under the MIT license, see LICENSE.txt

import os
from setuptools import setup, find_packages, Extension

extension = Extension("tradesocket", ["src/tradesocket.c"])

setup(
    name='tradesocket',
    version = '1.0.0',
    description = 'Allows sending of unix sockets over a unix socket.',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Topic :: Utilities',
    ],
    keywords = 'unix socket',
    author = 'Brantley Harris',
    author_email = 'deadwisdom@gmail.com',
    url = '',
    license = 'MIT',
    ext_modules = [extension],
    zip_safe = True,
    test_suite="tests.BasicTest"
)