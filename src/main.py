#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import constants
import time
import daemon.pidfile
import daemon

from zsh_weather import get_weather_info


def weather_main():
    result = get_weather_info()
    if result:
        with file(constants.DATA_PATH_FORMAT.format('weather'), mode='w+') as f:
            f.write(result)


def main():
    schedule.every(int(constants.CONFIG.get('WEATHER_INTERVAL'))).minutes.do(weather_main)
    weather_main()  # Run the function instantly and then schedule
    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == '__main__':
    with daemon.DaemonContext(pidfile=daemon.pidfile.PIDLockFile(constants.PID_PATH)):
        main()
