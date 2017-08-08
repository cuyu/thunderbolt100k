#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import constants
import time
import daemon.pidfile
import daemon
import os
import argparse
from thunderbolt100k.libs.common import write_conf, load_conf
import sys
from thunderbolt100k import __VERSION__
from thunderbolt100k.widgets import *  # Import all the widgets


def widget_main(widget):
    result = widget.fetch()
    if result:
        with file(constants.DATA_PATH_FORMAT.format(widget.__name__.replace('thunderbolt100k.widgets.', '')), mode='w+') as f:
            f.write(result)


def polling():
    for m in sys.modules['thunderbolt100k.widgets'].modules:
        if m.endswith('__init__.py'):
            continue

        widget_name = os.path.basename(m).replace('.py', '')
        widget = getattr(sys.modules['thunderbolt100k.widgets'], widget_name)
        if constants.CONFIG.get('{0}_INTERVAL'.format(widget.__name__.upper())):
            interval = int(constants.CONFIG.get('{0}_INTERVAL'.format(widget_name.upper())))
        else:
            interval = 5  # Default is 5 min if not specified
        schedule.every(interval).minutes.do(widget_main, widget)
        widget_main(widget)  # Run the function instantly and then schedule
    while True:
        schedule.run_pending()
        time.sleep(60)


def init_zshrc():
    import fileinput

    exist_conf = load_conf()
    if exist_conf:
        print('Thunderbolt100k has initialized before, delete the corresponding contents in `~/.zshrc` and try again')
        return

    # Set default settings
    print('Initializing default settings...')
    write_conf('VERSION', __VERSION__, first_write=True)
    for key in constants.DEFAULT_CONFIG:
        write_conf(key, constants.DEFAULT_CONFIG[key])

    # Bind polling command to a custom PL9K element
    write_conf('POWERLEVEL9K_CUSTOM_POLLING', '"thunderbolt100k polling"', without_prefix=True)

    elements_names = ['custom_polling']
    # Set PL9K custom command
    for m in sys.modules['thunderbolt100k.widgets'].modules:
        if m.endswith('__init__.py'):
            continue
        widget_name = os.path.basename(m).replace('.py', '')
        print('Initializing [{0}] widget...'.format(widget_name))
        widget = getattr(sys.modules['thunderbolt100k.widgets'], widget_name)
        write_conf('POWERLEVEL9K_CUSTOM_{0}'.format(widget_name.upper()),
                   '"thunderbolt100k display {0}"'.format(widget_name), without_prefix=True)

        elements_names.append('custom_{0}'.format(widget_name))
        # Ask for extra info for each widgets
        result = widget.user_input()
        for k in result:
            write_conf(k, result[k])

    # Add the custom elements to PL9K
    home = os.path.expanduser("~")
    path = os.path.join(home, '.zshrc')
    for line in fileinput.input(path, inplace=True):
        if line.startswith('POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS'):
            print(line.replace(')', ' {0})'.format(' '.join(elements_names))).rstrip())
        else:
            print(line.rstrip())
    fileinput.close()

    print('Initialization done! Open a new shell session and enjoy the view!')
    print('You may also want to rearrange the widgets locations by editing `POWERLEVEL9K_LEFT_PROMPT_ELEMENTS` and \n' +
          '`POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS` in `~/.zshrc` file')
    print('If you want to set configurations for THUNDERBOLT100K, please refer to https://github.com/cuyu/thunderbolt100k#configuration')


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='A cmdline tool to enhance PL9K theme for ZSH\n')
    subparsers = parser.add_subparsers(help='Use {subcommand} -h for each subcommand\'s optional arguments details',
                                       dest='command')
    subparsers.add_parser('init', help='Init the settings in `~/.zshrc` file')
    subparsers.add_parser('polling', help='Start the polling daemon process')
    display_parser = subparsers.add_parser('display', help='Print the corresponding info on the terminal')
    display_parser.add_argument('widget', help='The widget to display, e.g. weather')

    args = parser.parse_args()
    if args.command == 'polling':
        with daemon.DaemonContext(pidfile=daemon.pidfile.PIDLockFile(constants.PID_PATH)):
            polling()
    elif args.command == 'display':
        widgets = sys.modules['thunderbolt100k.widgets']
        assert hasattr(widgets, args.widget), 'There is no widget called {0}'.format(args.widget)
        assert hasattr(getattr(widgets, args.widget),
                       'display'), 'The widget {0} must contains a `display` method'.format(args.widget)
        result = getattr(widgets, args.widget).display()
        if result:
            print(result)
    elif args.command == 'init':
        init_zshrc()


if __name__ == '__main__':
    main()
