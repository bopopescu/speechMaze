import pygame
import threading
import time
from star_algorithm import Node
from star_algorithm import Path
from star_algorithm import Board
from star_algorithm import heuristic
from star_algorithm import setUp
#from printVoice import escuchar

import webbrowser
import string
import speech_recognition as SR
import os
#import time


escuchando = True;
v_fil = 12
v_col = 12

# obtain audio 
r = SR.Recognizer()

def comando(cadena):
        print("hola")
        global v_fil
        cadena = cadena.lower()
        entrada = cadena.split()
        if(entrada[1] == "columnas"):
            print(entrada[0])
        elif(entrada[1] == "filas" or entrada[1] == "pilas"):
            try:
                v_fil = int(entrada[0])
            except ValueError:
                print("Sorry")
                
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
                   os.system("say 'Perdon no entiendo'")
                except SR.RequestError as e:
                    os.system("say 'I could not request results from Google Speech Recognition service. Do you want error report?'")
 
#Star algorithm

diagonals = True

#Screen
v_square  = 30
v_margen = 5
board = []
star_board = []
grid = []
v_dimX = (v_fil+1)*v_square
v_dimY = (v_col+1)*v_square
update = False


#Images
Grass = pygame.transform.scale(pygame.image.load("images//grass.jpg"),(v_square,v_square))
Stone = pygame.transform.scale(pygame.image.load("images//rock.png"),(v_square,v_square))
Ground = pygame.transform.scale(pygame.image.load("images//ground.png"),(v_square,v_square))
Wood = pygame.transform.scale(pygame.image.load("images//wood.png"),(v_square,v_square))
Grill = pygame.transform.scale(pygame.image.load("images//grill.jpg"),(v_square,v_square))
Pig = pygame.transform.scale(pygame.image.load("images//pig.png"),(v_square,v_square))
PigTired = pygame.transform.scale(pygame.image.load("images//pigTired.jpg"),(v_square,v_square))

hiloVoz = threading.Thread(target = escuchar)

hiloVoz.start()

        
#Initial board
for row in range(v_fil):
    grid.append([])
    for column in range(v_col):
        grid[row].append(0)

        
pygame.init()
window = pygame.display.set_mode([v_dimY,v_dimX])
pygame.display.set_caption("speechMaze")
clock = pygame.time.Clock()


def dibujar():
    point_end = False
    point_start = False
    path = []
    v_done = False
    end = () 
    start = ()
    global grid
    global v_fil
    global v_col

    while not v_done:
        if end != () and start != ():
            grid2 = []
            for row in range(v_fil+1):
                temp = []
                for column in range(v_col+1):
                    node = Node(row, column, " ", heuristic((row, column), end))
                    temp.append(node)
                grid2.append(temp)

            #Inicial star_board
            star_board = setUp(v_fil,v_col,start,end,grid2,diagonals)
            for node in star_board.paths[0].pathArray:
                path.append([node.i,node.j])

            #Update grid with solution
            for row in range(v_fil):
                for column in range(v_col):
                    if(star_board.board[row][column].state == "b" ):
                        grid[row][column] = 3
                    if(star_board.board[row][column].state == "o" ):
                        grid[row][column] = 2
            v_fil = 20
            v_col = 20
            grid = []
            for row in range(v_fil):
                grid.append([])
                for column in range(v_col):
                    grid[row].append(0)
            end = ()
            start = ()
                    
      
        #Grid events
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                v_done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (v_square + v_margen)
                row = pos[1] // (v_square + v_margen)
                if point_end == False and point_start == False:
                    grid[row][column] = 1
                    start = (row,column)
                    point_start = True
                else:
                    if point_end == False:
                        grid[row][column] = 1
                        end = (row,column)
                        point_end = True
                        
                print("Click ", pos, "Coordenadas de la retícula: ", row, column)
            #Reload
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for row in range(v_fil):
                        for column in range(v_col):
                            grid[row][column] = 0
                    point_end = False
                    point_start = False
       
            for row in range(v_fil):
                for column in range(v_col):
                    window.blit(Grass, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 1: #start,end
                        window.blit(Ground, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 2: #road
                        window.blit(Grill, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 3: #block
                        window.blit(Stone, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))                

            if path != []:  #simulate pig walking
                for i in path:
                    print(i)
                    v_len = len(path)-1 
                    if(i == path[v_len]):
                        window.blit(PigTired, ((v_margen+v_square) * i[1] + v_margen,(v_margen+v_square) * i[0] + v_margen))
                    else:
                        window.blit(Pig, ((v_margen+v_square) * i[1] + v_margen,(v_margen+v_square) * i[0] + v_margen))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    window.blit(Grill, ((v_margen+v_square) * i[1] + v_margen,(v_margen+v_square) * i[0] + v_margen))
                    pygame.display.update()                              
                path = []
                
                    

                      
        clock.tick(60)
        pygame.display.flip()
                
        

    pygame.quit()



dibujar()
