#!/usr/bin/env python3
import os
import argparse
import configparser
import gntp.notifier
import logging
logging.basicConfig(level=logging.ERROR)

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.growl-notifier.cfg'))

title = config.get("utman", "title", fallback=None)
description = config.get("utman", "description", fallback=None)
application = config.get("utman", "application", fallback="Growl Notifier")
icon = config.get("utman", "icon", fallback=None)
hostname = config.get("utman", "hostname", fallback=None)
password = config.get("utman", "password", fallback=None)


parser = argparse.ArgumentParser()
parser.add_argument("title", help="title of notification")
parser.add_argument("--description", help="a longer description")
parser.add_argument("--application", help="name of application")
parser.add_argument("--icon", help="icon to display")
parser.add_argument("--hostname", help="host where growl is running")
parser.add_argument("--password", help="password to the growl service")
args = parser.parse_args()

title = args.title if args.title else title
hostname = args.hostname if args.hostname else hostname
description = args.description if args.description else description
password = args.password if args.password else password
application = args.application if args.application else application
icon = args.icon if args.icon else icon

growl = gntp.notifier.GrowlNotifier(
        applicationName = application,
        notifications = ["utman"],
        defaultNotifications = ["utman"],
        hostname = hostname,
        password = password
)
growl.register()

growl.notify(
    noteType = "utman",
    title = title,
    description = description,
    icon = icon,
    sticky = False,
    priority = 1,
)
