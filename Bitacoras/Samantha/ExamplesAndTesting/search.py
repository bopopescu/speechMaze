
import webbrowser
import string
import speech_recognition as SR

# obtain audio 
r = SR.Recognizer()
with SR.Microphone() as source:

    print("Hello, say search!")
    audio = r.listen(source)

if "search" in r.recognize_google(audio):
    # obtain audio from the microphone
    r5 = SR.Recognizer()
    
    with SR.Microphone() as source:
        print("what would you like me to search? ")
        audio5 = r5.listen(source)
        url5= r5.recognize_google(audio5)

        try:
            print("Google Speech Recognition thinks you said " + r5.recognize_google(audio5))
            webbrowser.open_new("https://duckduckgo.com/"+url5)
        except SR.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except SR.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))