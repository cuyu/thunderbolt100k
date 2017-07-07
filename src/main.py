#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import constants
import time

from zsh_weather import get_weather_info
from load_conf import load_conf


def weather_main():
    # Read configuration first
    constants.CONFIG = load_conf()

    result = get_weather_info()
    with file(constants.DATA_PATH_FORMAT.format('weather'), mode='w+') as f:
        f.write(result)


def before_all():
    # Read configuration first
    constants.CONFIG = load_conf()

    # Use default config if not specified
    for key in constants.DEFAULT_CONFIG:
        if key not in constants.CONFIG:
            constants.CONFIG[key] = constants.DEFAULT_CONFIG[key]


if __name__ == '__main__':
    before_all()
    schedule.every(int(constants.CONFIG.get('WEATHER_INTERVAL'))).minutes.do(weather_main)
    while True:
        schedule.run_pending()
        time.sleep(1)
