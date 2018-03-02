#!/usr/bin/env python3
import os
import argparse
import configparser
import gntp.notifier
import logging
logging.basicConfig(level=logging.ERROR)

# This should be in "utman"'s config file in section growlnotify.py(?)
config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.utman.cfg'))

title = config.get("utman", "title", fallback="growlnotify")
messagetext = config.get("utman", "description", fallback=None)
application = config.get("utman", "application", fallback="Growlnotify")
icon = config.get("utman", "icon", fallback=None)
host = config.get("utman", "hostname", fallback=None)
password = config.get("utman", "password", fallback=None)


parser = argparse.ArgumentParser()
parser.add_argument("--title", help="notification title")
parser.add_argument("--id", help="notification id")
parser.add_argument("--sticky", help="should the notification be sticky")
parser.add_argument("--priority", help="notification priority")
parser.add_argument("--icon", help="icon to display for the notification")
parser.add_argument("--application", help="name of application sending the notification")
parser.add_argument("--appicon", help="icon of the application sending the notification, only applicable if '--type' is also given")
parser.add_argument("--types", help="register application first, followed by a comma-separated list of notification types to register")
parser.add_argument("--type", help="notification name/type")
parser.add_argument("--callback", help="callback URL which will be opened if the notification is clicked")
parser.add_argument("--host", help="host where growl is running")
parser.add_argument("--port", help="port to use")
parser.add_argument("--password", help="password required to send notification to growl service on remote host")
parser.add_argument("--encryption", help="encryption to use, valid values NONE|DES|3DES|AES, if value other than NONE, then --password and --hash needs to be given")
parser.add_argument("--hash", help="hashing algorithm to use, valid values MD5|SHA1|SHA256|SHA512, only used if --password is given")
parser.add_argument("--silent", help="suppress response output")
parser.add_argument("messagetext", help="text of the notification")

args = parser.parse_args()

title = args.title if args.title else title
host = args.host if args.host else host
password = args.password if args.password else password
application = args.application if args.application else application
icon = args.icon if args.icon else icon
messagetext = args.messagetext if args.messagetext else messagetext

growl = gntp.notifier.GrowlNotifier(
        applicationName = application,
        notifications = ["utman"],
        defaultNotifications = ["utman"],
        hostname = host,
        password = password
)
growl.register()

growl.notify(
    noteType = "utman",
    title = title,
    description = messagetext,
    icon = icon,
    sticky = False,
    priority = 1
)
