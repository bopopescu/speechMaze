# Install PyGame

From https://stackoverflow.com/questions/42008679/cant-install-pygame-on-mac

## MacOS

1. Install homebrew. Go into terminal and paste 

**ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”**

then hit enter.

1. Paste the following into terminal, hitting enter after each line:

**brew install python** ( **brew install python3** for python3 users )

**brew install mercurial**

**brew install sdl sdl_image sdl_mixer sdl_ttf portmidi**

**brew tap homebrew/headonly** (if you have any trouble here, try **brew install –HEAD smpeg**instead, with two dashes/hyphens before the HEAD option)

**brew install smpeg**

**sudo -H pip install hg+http://bitbucket.org/pygame/pygame** (You will have to enter your password, and you must be an admin. Python3 users should use **sudo -H pip3 install hg+http://bitbucket.org/pygame/pygame**

