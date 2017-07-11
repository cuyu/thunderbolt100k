#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from src import __VERSION__


setuptools.setup(
    name='thunderbolt100k',
    version=__VERSION__,
    description='A cmdline tool to poll some info into local env for later use',
    packages=['src'],
    include_package_data=True,  # Include the template files
    test_suite='tests',
    author='Curtis Yu',
    author_email='cuyu@splunk.com',
    install_requires=[
        'schedule',
        'requests',
        'python-daemon',
    ],
    url='https://github.com/cuyu/thunderbolt100k',
    entry_points={
        "console_scripts": [
            "_thunderbolt100k = src.main:main",
        ],
    },
)
