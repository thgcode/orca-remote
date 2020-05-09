# Orca-Remote

Orca-Remote is a plugin that makes it possible to the Orca and NVDA screen
readers to communicate.

Currently, the plugin only supports sending Orca speech to NVDA, but more
features will be added in the future.

## Warnings

Don't use this code in production (this is alpha quality software). The code will be improved with time. At this
time it is just a proof-of-concept.

Don't install it unless you know what you are doing. Installation failures can
render Orca speech unusable.

At this time, the code is intended to be used on a Virtual machine. Currently,
NVDA sending keys to Orca is not implemented.

## How to use / Installation

First, set up an NVDA Remote server on your local machine. Use the `control
another machine` option. Make note of the
settings you use on the connection dialog, as you will use them on the
installer.

Next, execute the provided install script, passing as parameters your NVDA Remote server IP
address, the port and the key. This will copy the plugin to your Orca user
directory. If you have any Orca customizations set up, the script will
back then up for you, as the plugin uses this file to connect to the NVDA
remote server.

Lastly, if all goes well, use the `orca --replace` command to replace Orca and
make it connect to the NVDA Remote server.

## Credits

* Some parts of this code were based from [NVDA Remote][nvdaremote_repo]

## License

As this code uses parts of NVDA Remote, it is licensed under the GNU GPL
Version 2.

[nvdaremote_repo]:https://github.com/nvdaremote/nvdaremote
