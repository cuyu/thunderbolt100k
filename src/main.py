#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import constants
import time

from zsh_weather import get_weather_info


def weather_main():
    result = get_weather_info()
    with file(constants.DATA_PATH_FORMAT.format('weather'), mode='w+') as f:
        f.write(result)


if __name__ == '__main__':
    schedule.every(int(constants.CONFIG.get('WEATHER_INTERVAL'))).minutes.do(weather_main)
    while True:
        schedule.run_pending()
        time.sleep(10)
