
import webbrowser
import string
import speech_recognition as SR
import os
import time

escuchando = True;

# obtain audio 
r = SR.Recognizer()

def comando(cadena):
        print("hola")
        cadena = cadena.lower()
        entrada = cadena.split()
        if(entrada[1] == "columnas"):
                print(entrada[0])
        elif(entrada[1] == "filas" or entrada[1] == "pilas"):
                print(entrada[0])
        elif(entrada[0] == "tamaño"):
                print(entrada[1])
        elif(entrada[0] == "inicio"):
                print(entrada[1])
        elif(entrada[0] == "final"):
                print(entrada[1])
        elif(entrada[0] == "limpiar"):
                print(entrada[1])
        

def escuchar():
        global escuchando
        global r
        
        while (escuchando == True):
            time.sleep(1)
            with SR.Microphone() as source:
                os.system("say 'Esperando instrucción'")
                
                audio5 = r.listen(source)
                try:
                    audio = r.recognize_google(audio5,language = "es-CR")
                    comando(audio)
                    #print(audio)
                except SR.UnknownValueError:
                   os.system("say 'Bacon could not understand you'")
                except SR.RequestError as e:
                    os.system("say 'I could not request results from Google Speech Recognition service. Do you want error report?'")


        
                
                    
            
        
        
    
    







