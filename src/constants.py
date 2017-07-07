#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 7/7/17
"""
CONFIG = dict()
DEFAULT_CONFIG = {
    'WEATHER_INTERVAL': '5',
    'WEATHER_INFO': '(condition temp last_update)'
}
DATA_PATH_FORMAT = '/tmp/thunderbolt100k_{0}.data'
PID_PATH = '/tmp/thunderbolt100k.pid'