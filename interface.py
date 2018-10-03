#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygame
import threading
import time
import random
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


# obtain audio 
r = SR.Recognizer()

def comando(cadena):
        print(cadena)
        cadena = cadena.lower()
        entrada = cadena.split()
        if(len(entrada)>=2):
            if(entrada[1] == "columnas"):
                try:
                    col = int(entrada[0])
                    update_col(col)
                    print(col)
                except ValueError:
                    print("Sorry")
            elif(entrada[1] == "filas" or entrada[1] == "pilas"):
                try:
                    fil = int(entrada[0])
                    update_fil(fil)
                    print(fil)
                except ValueError:
                    print("Sorry")
            elif(entrada[0] == "tamaño"):
                try:
                    a = int(entrada[1])
                    update_tam(a)
                    print(a)
                except ValueError:
                    print("Sorry")
            elif(entrada[0] == "inicio" or entrada[0] =="inició"):
                print(entrada)
                
        else:    
            if(entrada[0] == "limpiar"):
                global update
                update = True
                print(entrada[0])
        

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
v_fil = 8
v_col = 8
v_square  = 50
diagonals = True
end = () 
start = ()
update = False
start_maze = False


#Grid variables
grid = []
point_end = False
point_start = False
v_margen = 5
star_board = []

#Images
Grass = pygame.transform.scale(pygame.image.load("images//grass.jpg"),(v_square,v_square))
Stone = pygame.transform.scale(pygame.image.load("images//rock.png"),(v_square,v_square))
Ground = pygame.transform.scale(pygame.image.load("images//ground.png"),(v_square,v_square))
Wood = pygame.transform.scale(pygame.image.load("images//wood.png"),(v_square,v_square))
Grill = pygame.transform.scale(pygame.image.load("images//grill.jpg"),(v_square,v_square))
Pig = pygame.transform.scale(pygame.image.load("images//pig.png"),(v_square,v_square))
PigTired = pygame.transform.scale(pygame.image.load("images//pigTired.jpg"),(v_square,v_square))
    

    

        
pygame.init()
window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
pygame.display.set_caption("speechMaze")
 
clock = pygame.time.Clock()



def reload_grid():
    global grid
    global window
    global point_end
    global point_start
    global v_fil
    global v_col
    grid = []
    for row in range(v_fil):
        grid.append([])
        for column in range(v_col):
            grid[row].append(0)
    point_end = False
    point_start = False


def update_col(col):
    global v_col
    global update    
    v_col = col
    update = True
    

def update_fil(fil):
    global v_fil
    global update
    v_fil = fil
    update = True
    
    

def update_tam(tam):
    global update
    global v_square
    v_square = tam
    update = True

    

def event_click():
    global grid
    global point_start
    global point_end
    global v_margen
    global end
    global start
    pos = pygame.mouse.get_pos()
    column = pos[0] // (v_square + v_margen)
    row = pos[1] // (v_square + v_margen)
    if column == 0 and row == 0 :
        update_col(20)
            
    if point_end == False and point_start == False:
        grid[row][column] = 1
        start = (row,column)
        point_start = True
    else:
        if point_end == False:
            grid[row][column] = 1
            end = (row,column)
            point_end = True

def bacon_moving(v_margen,v_square,path):  
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


def make_route(path,blocks):
    global star_board
    grid2 = []
    for row in range(v_fil+1):
        temp = []
        for column in range(v_col+1):
            node = Node(row, column, " ", heuristic((row, column), end))
            temp.append(node)
        grid2.append(temp)

    #Inicial star_board
    star_board = setUp(v_fil,v_col,start,end,grid2,diagonals,blocks)

    for node in star_board.paths[0].pathArray:
        path.append([node.i,node.j])


def draw_route():
    global grid
    global star_board
    #Update grid with solution
    for row in range(v_fil):
        for column in range(v_col):
            if(star_board.board[row][column].state == "o" ):
                grid[row][column] = 2
            if(star_board.board[row][column].state == "b" ):
                grid[row][column] = 3 

def make_blocks():
    global v_gil
    global v_col
    global end
    global start
    global grid
    blocks = []
    for i in range(v_fil):
        for j in range(v_col):
            ran = random.randint(1,v_fil*v_col)
            ran2 = v_fil*v_col//6
            if(ran < ran2 and start[0] != i and end[0] != i and start[1] != j and end[1] != j):
                blocks.append([i,j])
                grid[i][j] = 3
    return blocks


def draw_grid():
    global v_fil
    global v_col
    global grid
    global v_margen
    global v_square
    for row in range(v_fil):
        for column in range(v_col):
            window.blit(Grass, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
            if grid[row][column] == 1: #start,end
                window.blit(Ground, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
            if grid[row][column] == 2: #road
                window.blit(Grill, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
            if grid[row][column] == 3: #block
                window.blit(Stone, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))

def draw():
    global end
    global start
    global v_fil
    global v_col
    global grid
    global point_start
    global point_end
    global v_margen
    global window
    global update
    global start_maze

    v_done = False
    path = []
    board = []
    star_board = []
    blocks = []

    hiloVoz = threading.Thread(target = escuchar)
    hiloVoz.start()

    #Initial board
    for row in range(v_fil):
        grid.append([])
        for column in range(v_col):
            grid[row].append(0)

        
    while not v_done:

        #Make route with star algorith
        if end != () and start != ():
           blocks = make_blocks()
           make_route(path,blocks)
           end = ()
           start = ()
            

        #Actualizacion
        if (update== True):
                window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
                reload_grid()
                update = False
                
                

            
        #Grid events
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                v_done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event_click()

                        
            #Reload
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reload_grid()
                if event.key == pygame.K_s:
                    start_maze = True

            #Dibujar cuadricula
            draw_grid()

            #simulate pig walking
            if start_maze == True:
                draw_route()
                draw_grid()
                bacon_moving(v_margen,v_square,path)
                path = []
                start_maze = False
                end = ()
                start = ()

                               
                      
        clock.tick(60)
        pygame.display.flip()
                
        
    pygame.quit()


draw()




