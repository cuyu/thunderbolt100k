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


schedule.every(int(constants.CONFIG.get('WEATHER_INTERVAL') or 5)).minutes.do(weather_main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
