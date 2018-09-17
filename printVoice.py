
import webbrowser
import string
import speech_recognition as SR
import os

# obtain audio 
r = SR.Recognizer()
with SR.Microphone() as source:
    #print("Hello, say go \n or ##bye## for close!")
    os.system("say 'Whats up?!, Do I work or not?'")
    audio = r.listen(source)

if "bye" in r.recognize_google(audio):
    os.system("say 'chao-chao, salshishon'")
    exit()

if "bacon" in r.recognize_google(audio):
    os.system("say 'Hey you!, What i am going to print?'")
    r5 = SR.Recognizer()
    with SR.Microphone() as source:
        audio5 = r5.listen(source)
        try:
            #print("Google Speech Recognition thinks you said \n\t\t\t" + r5.recognize_google(audio5))
            os.system("say 'You said'")
            print(r5.recognize_google(audio5))
        except SR.UnknownValueError:
            os.system("say 'Bacon could not understand you'")
        except SR.RequestError as e:
            os.system("say 'I could not request results from Google Speech Recognition service. Do you want error report?'")
            
            rc = SR.Recognizer()
            with SR.Microphone() as source:
                audio = rc.listen(source)
                if "yes" in rc.recognize_google(audio):
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                if "no" in rc.recognize_google(audio):
                    os.system("say 'so! do I'")


