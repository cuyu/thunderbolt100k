#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


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
