#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libs.common import load_conf

CONFIG = dict()
DEFAULT_CONFIG = {
    'WEATHER_INTERVAL': '5',
    'WEATHER_INFO': '(condition temp last_update)',
    'WEATHER_RAIN_COLOR': '153',
    'WEATHER_SUN_COLOR': '172',
    'WEATHER_CLOUD_COLOR': '250',
    'WEATHER_OVERCAST_COLOR': '244',
    'WEATHER_SNOW_COLOR': '60',
    'WEATHER_THUNDER_COLOR': '226',
    'WEATHER_DEFAULT_COLOR': '195',
    'WEATHER_HIGH_TEMP_COLOR': '196',
    'WEATHER_MIDDLE_TEMP_COLOR': '209',
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
