#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def pl9k_color(color):
    return '%F{' + color + '}'


# Assume the conf location is '~/.zshrc'
def load_conf():
    home = os.path.expanduser("~")
    path = os.path.join(home, '.zshrc')
    config = dict()
    with file(path, mode='r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line.startswith('THUNDERBOLT100K'):
                key, value = line.split('=')
                # Remove the prefix in key and the quotation marks in the value
                config[key.split('THUNDERBOLT100K_')[1]] = value.replace('"', '').replace("'", '').strip()
    return config


def write_conf(key, value, replace_exist=False, first_write=False):
    home = os.path.expanduser("~")
    path = os.path.join(home, '.zshrc')

    if first_write:
        with file(path, mode='a') as f:
            f.write("############################\n# For THUNDERBOLT100K\n")
        write_conf(key, value, replace_exist)
    else:
        if replace_exist:
            raise NotImplementedError
        else:
            with file(path, mode='a') as f:
                f.write('THUNDERBOLT100K_{0}={1}\n'.format(key, value))
