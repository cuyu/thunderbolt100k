#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

from thunderbolt100k import __VERSION__

setuptools.setup(
    name='thunderbolt100k',
    version=__VERSION__,
    description='A cmdline tool to poll some info into local storage for later use',
    packages=setuptools.find_packages(),
    include_package_data=True,  # Include the template files
    test_suite='tests',
    author='Curtis Yu',
    author_email='icyarm@icloud.com',
    install_requires=[
        'schedule',
        'requests',
        'python-daemon',
    ],
    url='https://github.com/cuyu/thunderbolt100k',
    entry_points={
        "console_scripts": [
            "thunderbolt100k = thunderbolt100k.main:main",
        ],
    },
)
