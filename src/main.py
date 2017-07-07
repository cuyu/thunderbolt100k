#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time
import constants

from zsh_weather import get_weather_info
from load_conf import load_conf


def main():
    # Read configuration first
    constants.CONFIG = load_conf()

    result = get_weather_info()
    with file('/tmp/thunderbolt100k', mode='w+') as f:
        f.write(str(result))

schedule.every().minute.do(main)

if __name__ == '__main__':
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    main()