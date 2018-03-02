# Growlnotify in Python

Growl notification system for MacOS and Windows includes a public protocol
that allows arbitray programs and scripts to create notifications.

This is an implementation of the Growl utility `growlnotify` in Python.

I wanted to create this because the utility seems to be closed source
but the protocol is not, and it only exists on the supported platforms.

The aim is to be fully argument compatible with growlnotify on MacOS, and
possibly on some level also the Windows variant. Here's the output of
the Windows variant:

    Send a Growl notification to a local or remote host

    growlnotify [/t:title] [/id:id] [/s:sticky] [/p:priority] [/i:icon]
                [/a:application] [/ai:icon] [/r:type] [/n:type]
                [/cu:callbackurl]
                [/host:host] [/port:port]
                [/pass:password] [/enc:algorithm] [/hash:algorithm]
                [/silent:nooutput]
                messagetext

      [/t:title]            The notification title.
                            Use \n to specify a line break.
                            Use \\n for a literal '\n'.
                            Default: "growlnotify"

      [/id:id]              The notification id.
                            Default: ""

      [/s:sticky]           Indicates if the notification should be sticky.
                            Valid values: true|false
                            Default: false

      [/p:priority]         The notification priority.
                            Valid values: -2|-1|0|1|2
                            Default: 0

      [/i:icon]             The icon to show for the notification.
                            Must be a valid file type (png, jpg, gif, ico).
                            Can be any of the following:
                              - absolute url (http://domain/image.png)
                              - absolute file path (c:\temp\image.png)
                              - relative file path (.\folder\image.png) (relative
                                file paths must start with a dot (.) and are
                                relative to growlnotify's location
                            Note: Icons specified as urls will be passed as urls
                                  (links). Icons specified as local files (either
                                  absolute or relative) will be sent as binary
                                  data.
                            Default: no icon

      [/a:application]      The name of the application sending the notification.
                            The application must already be registered unless the
                            /r switch is included. The default 'growlnotify'
                            application does not need to be explicitly registered.
                            Default: growlnotify

      [/ai:appicon]                 The icon of the application being registered.
                                                    Only applicable if the /r switch is also passed.
                            Must be a valid file type (png, jpg, gif, ico).
                            Can be any of the following:
                              - absolute url (http://domain/image.png)
                              - absolute file path (c:\temp\image.png)
                              - relative file path (.\folder\image.png) (relative
                                file paths must start with a dot (.) and are
                                relative to growlnotify's location
                            Note: Icons specified as urls will be passed as urls
                                  (links). Icons specified as local files (either
                                  absolute or relative) will be sent as binary
                                  data.
                            Default: no icon

      [/r:type]             Register the application first.
                            'types' is a comma-separated list of the notification
                            types to register.
                            Default: application not automatically registered
                            Examples:
                                /r:"Some Notification"
                                /r:"Notification One","Notification Two","Notification Three"

      [/n:type]             The notification name/type.
                            Default: "General Notification"

      [/cu:callbackurl]     A callback url (will be opened if the notification is
                            clicked).
                            Default: no callback

      [/host:host]          The host address to send the notification to.
                            If any value other than 'localhost' or '127.0.0.1' is
                            provided, the host is considered a remote host and the
                            /pass switch must also be provided.
                            Default: localhost

      [/port:port]          The port to send the notification to.
                            Default: 23053

      [/pass:password]      The password required to send notifications.
                            A password is required to send a request to a remote
                            host. If /host is specified and is any value other than
                            'localhost' or '127.0.0.1', then /pass is also
                            required.
                            Default: no password

      [/enc:algorithm]      The encryption algorithm to use.
                            Valid values: NONE|DES|3DES|AES
                            If a value other than NONE is provided, the
                            /pass and /hash switches must also be included.
                            Default: NONE

      [/hash:algorithm]     The hashing algorithm to use.
                            Valid values: MD5|SHA1|SHA256|SHA512
                            This value is only used if the /pass switch is also
                            set.
                            Default: MD5

      [/silent:nooutput]    When run from the command line, indicates if response
                            output should be suppressed or not.
                            Valid values: true|false
                            Default: false

      messagetext                   The notification's text - Required
                            Use \n to specify a line break.
                            Use \\n for a literal '\n'.
