## **2018-09-16**



## Speech Recognition

https://pypi.org/project/SpeechRecognition/

## Install

Install Python from here: https://www.python.org/downloads/

Install pip

```bash
$ sudo easy_install pip3
```

Install Speech Recognition 

```bash
$ pip3 install SpeechRecognition
```

Check version

```bash
$ python
```

```python
import speech_recognition as sr

sr.__version__
```

It should show:

```python
'3.8.1'
```



## Class

Each `Recognizer` instance has seven methods for recognizing speech from an audio source using various APIs. These are:

- `recognize_bing()`: [Microsoft Bing Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
- `recognize_google()`: [Google Web Speech API](https://w3c.github.io/speech-api/speechapi.html)
- `recognize_google_cloud()`: [Google Cloud Speech](https://cloud.google.com/speech/) - requires installation of the google-cloud-speech package
- `recognize_houndify()`: [Houndify](https://www.houndify.com/) by SoundHound
- `recognize_ibm()`: [IBM Speech to Text](https://www.ibm.com/watson/services/speech-to-text/)
- `recognize_sphinx()`: [CMU Sphinx](https://cmusphinx.github.io/) - requires installing PocketSphinx
- `recognize_wit()`: [Wit.ai](https://wit.ai/)



### Google Web Speech API

Requirements

#### PyAudio

**Linux**

```bash
pip3 install pyaudio
```

#### PortAudio

http://www.portaudio.com/download.html

**Mac**

```bash
brew install portaudio
pip3 install pyaudio
```

#### OAuth2Client

```bash
$ pip3 install --upgrade oauth2client 
```

#### Google API

```bash
$ pip3 install --force-reinstall google-api-python-client
```

```bash
$ pip3 install --upgrade google-api-python-client
$ pip3 install --upgrade google-cloud
```



Follow:  https://cloud.google.com/sdk/docs/

Google Project ID: ia-speechmaze-2018



#### Run Example

https://www.youtube.com/watch?v=qNlKO0L4gMI

https://github.com/ChaseMathis/Speech-Recognition



# Text to speech

```python
import os

os.system("say 'string'")
```

### Con Libreria

```bash
$ sudo pip3 install pyttsx
```





# **2018-09-18**

1. Implement Google Text-to-Speech API
2. Say what it receive 

### Google Text-to-Speech API

From: https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/texttospeech/cloud-client

https://cloud.google.com/python/setup#installing_and_using_virtualenv

#### Install Dependencies

1. Clone python-docs-samples and change directory to the sample directory you want to use.

   > ```bash
   > $ git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
   > ```

2. Install [pip](https://pip.pypa.io/) and [virtualenv](https://virtualenv.pypa.io/) if you do not already have them. You may want to refer to the [Python Development Environment Setup Guide](https://cloud.google.com/python/setup) for Google Cloud Platform for instructions.

3. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

   > ```bash
   > $ virtualenv env
   > $ source env/bin/activate
   > ```

4. Install the dependencies needed to run the samples.

   > ```bash
   > $ pip install -r requirements.txt
   > ```



# **2018-09-20**

The Text-to-Speech function it's define with system library (``import os``) call by Python.



Command for function:

```python
import os

os.system("say 'What I want to say'")
```



In this ways, the voice which is speaking it's the system voice. In Microsoft Windows is going to be Cortana, in MacOS can be Siri or the want you choose for narration in Accesibility module of de MacOS settings.





# **2018-10-03**

User manual with screenshot of the last reviews of the program

# Links

https://pypi.org/project/SpeechRecognition/

https://www.youtube.com/watch?v=bp8WNm89E9g

https://realpython.com/python-speech-recognition/

https://cmusphinx.github.io/wiki/download/

https://cmusphinx.github.io/wiki/tutorialpocketsphinx/#installation-on-unix-system

http://www.portaudio.com/download.html

https://pythonspot.com/speech-recognition-using-google-speech-api/comment-page-1/

https://pythonprogramminglanguage.com/text-to-speech/

https://pythonprogramminglanguage.com/text-to-speech/