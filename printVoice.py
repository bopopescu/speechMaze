#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import webbrowser
import string
import speech_recognition as SR
import os
import time

escuchando = True;

# obtain audio 
r = SR.Recognizer()

def comando(cadena):
        cadena = cadena.lower()
        entrada = cadena.split()
        if(entrada[0] == "columnas"):
                print(entrada[0])
        elif(entrada[0] == "filas" or entrada[0] == "pilas"):
                print(entrada[0])
        elif(entrada[0] == "tamaño"):
                print(entrada[0])
        elif(entrada[0] == "inicio"):
                print(entrada[0])
        elif(entrada[0] == "final"):
                print(entrada[0])
        elif(entrada[0] == "limpiar"):
                print(entrada[0])
        else:
                pass
        

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
                    print(audio)
                    comando(audio)
                    #print(audio)
                except SR.UnknownValueError:
                   os.system("say 'Bacon could not understand you'")
                except SR.RequestError as e:
                    os.system("say 'I could not request results from Google Speech Recognition service. Do you want error report?'")

escuchar()
        
                
                    
            
        
        
    
    







