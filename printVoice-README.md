# printVoice.py

## Install requirements 

1. Python 3

   https://www.python.org/downloads/

2. Pip 3

   ```bash
   $ sudo easy_install pip3
   ```

   SpeechRecognition Library

   ```bash
   $ pip3 install SpeechRecognition
   ```

3. PyAudio

   ```bash
   $ pip3 install pyaudio
   ```

   PortAudio

   ```brew install portaudio``` or here http://www.portaudio.com/download.html

4. OAuth2Client

   ```bash
   $ pip3 install --upgrade oauth2client
   ```

   Google API Python Client

   ```bash
   $ pip3 install --force-reinstall google-api-python-client
   
   $ pip3 install --upgrade google-api-python-client
   
   $ pip3 install --upgrade google-cloud
   ```

5. Text to Speech is going on OS, so just ```import os```  is need on Python, no installations require

#### NOTE

Google Project ID: ia-speechmaze-2018 

If it ask you for permission let me know, because I think i will need your GMail



## Run

```bash
$ python3 printVoice.py
```

## Interaction

#### Positive

Bacon:	say 'Whats up?!, Do I work or not?

You:	Hello Bacon,  Hi Bacon or just Bacon

Bacon:	Hey you!, What i am going to print?

You:	*say something*

Bacon:	You said...

 and it print yours words.

#### Negative

Bacon:	say 'Whats up?!, Do I work or not?

You:	bye

Bacon:	Chao Chao