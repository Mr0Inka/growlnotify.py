#!/usr/bin/env python3
import os
import argparse
import gntp.notifier
import logging
logging.basicConfig(level=logging.ERROR)

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
parser.add_argument("messagetext", help="text of the notification")

# Unimplemented possible GNTP options
#parser.add_argument("--encryption", help="encryption to use, valid values NONE|DES|3DES|AES, if value other than NONE, then --password and --hash needs to be given")
#parser.add_argument("--hash", help="hashing algorithm to use, valid values MD5|SHA1|SHA256|SHA512, only used if --password is given")
#parser.add_argument("--id", help="notification id")
#parser.add_argument("--port", help="port to use")

args = parser.parse_args()

title = args.title if args.title else "Growl Notification"
host = args.host if args.host else "localhost"
password = args.password if args.password else None
application = args.application if args.application else "growlnotify.py"
icon = args.icon if args.icon else None
messagetext = args.messagetext if args.messagetext else None
type = args.type if args.type else "Notification"
sticky = args.sticky
url = args.url if args.url else None
priority = args.priority if args.priority else 1

growl = gntp.notifier.GrowlNotifier(
        applicationName = application,
        notifications = [type],
        defaultNotifications = [type],
        hostname = host,
        password = password
)
growl.register()

# Package image data?
if (icon and not icon.startswith("http")):
    try:
        icon = open(icon, 'rb').read()
    except IOError:
        icon = ""

growl.notify(
    noteType = type,
    title = title,
    description = messagetext,
    icon = icon,
    sticky = sticky,
    callback = url,
    priority = priority
)
