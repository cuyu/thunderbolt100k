#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


# Compare the given time stamp with current time and return how long has been passed since then
def compare_time(time_stamp, time_format):
    now = datetime.datetime.now()
    target_time = datetime.datetime.strptime(time_stamp, time_format)

    delta_time = now - target_time

    delta_minute = (delta_time.seconds / 60) % 60
    delta_hour = (delta_time.seconds / 3600) % 24
    delta_day = delta_time.days

    return delta_minute, delta_hour, delta_day


if __name__ == '__main__':
    # Example: python compare_time.py '2017-07-07 12:00' '%Y-%m-%d %H:%M'
    import sys

    print compare_time(sys.argv[1].replace('"', '').replace("'", ''), sys.argv[2])
