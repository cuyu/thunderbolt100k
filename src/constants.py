#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 7/7/17
"""
from libs.common import load_conf

CONFIG = dict()
DEFAULT_CONFIG = {
    'WEATHER_INTERVAL': '5',
    'WEATHER_INFO': '(condition temp last_update)',
    'WEATHER_RAIN_COLOR': 'blue',
    'WEATHER_SUN_COLOR': 'yellow',
    'WEATHER_CLOUD_COLOR': 'white',
    'WEATHER_OVERCAST_COLOR': 'grey',
    'WEATHER_SNOW_COLOR': 'white',
    'WEATHER_THUNDER_COLOR': 'yellow',
    'WEATHER_DEFAULT_COLOR': 'green',
    'WEATHER_HIGH_TEMP_COLOR': 'red',
    'WEATHER_MIDDLE_TEMP_COLOR': 'yellow',
    'WEATHER_LOW_TEMP_COLOR': 'blue',
    'WEATHER_SHOW_UPDATE_TIME': '120',
    'WEATHER_UPDATE_TIME_COLOR': 'red',
}
DATA_PATH_FORMAT = '/tmp/thunderbolt100k_{0}.data'
PID_PATH = '/tmp/thunderbolt100k.pid'


def init():
    global CONFIG
    # Read configuration first
    CONFIG = load_conf()

    # Use default config if not specified
    for key in DEFAULT_CONFIG:
        if key not in CONFIG:
            CONFIG[key] = DEFAULT_CONFIG[key]


init()
