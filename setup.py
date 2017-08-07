#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from setuptools.command.install import install
from subprocess import call

from thunderbolt100k import __VERSION__


class CustomInstallCommand(install):
    """Customized setuptools install command"""

    def run(self):
        install.run(self)


setuptools.setup(
    name='thunderbolt100k',
    version=__VERSION__,
    description='A cmdline tool to poll some info into local env for later use',
    packages=['thunderbolt100k'],
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
            "thunderbolt100k = thunderbolt100k.main:main",
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
)
