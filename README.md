# Growlnotify in Python

Growl notification system for MacOS and Windows includes a public protocol
that allows arbitray programs and scripts to create notifications.

This is an implementation of the Growl utility `growlnotify` in Python.

I wanted to create this because the utility seems to be closed source
and it only exists on the supported platforms. But the protocol is
open, and even have a Python API.

Since the Windows and Mac variants are quite inconsistent, I've made
no attempt at making this compatible to either. Here's the current
options:

    usage: growlnotify.py [-h] [--title TITLE] [--sticky] [--priority PRIORITY]
                          [--icon ICON] [--application APPLICATION]
                          [--appicon APPICON] [--type TYPE] [--url URL]
                          [--host HOST] [--password PASSWORD]
                          messagetext

    positional arguments:
      messagetext           text of the notification

    optional arguments:
      -h, --help            show this help message and exit
      --title TITLE         notification title (default: 'Growl Notification')
      --sticky              make notification sticky
      --priority PRIORITY   notification priority (default: 1)
      --icon ICON           icon to display for the notification
      --application APPLICATION
                            name of application sending the notification (default:
                            'growlnotify.py')
      --appicon APPICON     icon of the application sending the notification
      --type TYPE           notification type (default: 'Notification')
      --url URL             callback URL which will be opened if the notification
                            is clicked
      --host HOST           host where growl is running (default: localhost)
      --password PASSWORD   password, if required to send notification to growl
                            service on remote host
