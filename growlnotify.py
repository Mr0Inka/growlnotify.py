#!/usr/bin/env python3
import os
import argparse
import configparser
import logging
logging.basicConfig(level=logging.ERROR)
import gntp.notifier

CONFIG_FILE=os.path.expanduser('~/.growlnotifyrc')
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as f:
        config_string = '[growlnotify]\n' + f.read()
else:
    config_string = '[growlnotify]\n'

config = configparser.ConfigParser()
config.read_string(config_string)

parser = argparse.ArgumentParser()
parser.add_argument("--title", help="notification title (default: 'Growl Notification')")
parser.add_argument("--sticky", help="make notification sticky", action="store_true")
parser.add_argument("--priority", help="notification priority (default: 1)")
parser.add_argument("--icon", help="icon to display for the notification")
parser.add_argument("--application", help="name of application sending the notification (default: 'growlnotify.py')")
parser.add_argument("--appicon", help="icon of the application sending the notification")
parser.add_argument("--type", help="notification type (default: 'Notification')")
parser.add_argument("--url", help="callback URL which will be opened if the notification is clicked")
parser.add_argument("--host", help="host where growl is running (default: localhost)")
parser.add_argument("--password", help="password, if required to send notification to growl service on remote host")
parser.add_argument("message", help="text of the notification")

# Unimplemented possible GNTP options
#parser.add_argument("--encryption", help="encryption to use, valid values NONE|DES|3DES|AES, if value other than NONE, then --password and --hash needs to be given")
#parser.add_argument("--hash", help="hashing algorithm to use, valid values MD5|SHA1|SHA256|SHA512, only used if --password is given")
#parser.add_argument("--id", help="notification id")
#parser.add_argument("--port", help="port to use")

args = parser.parse_args()

title = args.title if args.title else config.get('growlnotify', 'title', fallback="Growl Notification")
host = args.host if args.host else config.get('growlnotify', 'host', fallback="localhost")
password = args.password if args.password else config.get('growlnotify', 'password', fallback=None)
application = args.application if args.application else config.get('growlnotify', 'application', fallback="growlnotify.py")
icon = args.icon if args.icon else config.get('growlnotify', 'icon', fallback=None)
message = args.message if args.message else config.get('growlnotify', 'message', fallback=None)
type = args.type if args.type else config.get('growlnotify', 'type', fallback="Notification")
sticky = args.sticky
url = args.url if args.url else config.get('growlnotify', 'url', fallback=None)
priority = args.priority if args.priority else config.get('growlnotify', 'priority', fallback=1)

if host != "localhost" and password is None:
    print("ERROR: --password is required if contacting remote service")
    quit()

growl = gntp.notifier.GrowlNotifier(
        applicationName = application,
        notifications = [type],
        defaultNotifications = [type],
        hostname = host,
        password = password
)
try:
    growl.register()
except gntp.errors.NetworkError as e:
    print("ERROR: Could not contact Growl service on host '{}'".format(host))
    quit()

# Package image data?
if (icon and not icon.startswith("http")):
    try:
        icon = open(icon, 'rb').read()
    except IOError:
        icon = ""

growl.notify(
    noteType = type,
    title = title,
    description = message,
    icon = icon,
    sticky = sticky,
    callback = url,
    priority = priority
)
