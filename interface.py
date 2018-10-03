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


escuchando = True


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
v_done = False

# obtain audio 
r = SR.Recognizer()

def comando(cadena):
    print(cadena)
    cadena = cadena.lower()
    entrada = cadena.split()
    global update
    global blocks
    if(len(entrada)>=2):
        if(entrada[1] == "columnas"):
            try:
                col = int(entrada[0])
                update_col(col)
                print(col)
                os.system("say 'Actualizando columnas'")
            except ValueError:
                os.system("say 'No entendi'")
        elif(entrada[1] == "filas" or entrada[1] == "pilas"):
            try:
                fil = int(entrada[0])
                update_fil(fil)
                print(fil)
                os.system("say 'Actualizando filas'")
            except ValueError:
                os.system("say 'No entendi'")
        elif(entrada[0] == "diagonal"):
            try:
                global diagonals
                if(entrada[1] == "si"):
                    diagonals = True
                    os.system("say 'Habilitando diagonales'")
                if(entrada[1] == "no"):
                    diagonals = False
                    os.system("say 'Deshabilitando diagonales'")
            except ValueError:
                os.system("say 'No entendi'")
        elif(entrada[0] == "bloque"): #tamano
            try:
                a = int(entrada[1])
                update_tam(a)
                print(a)
                os.system("say 'Actualizando largo de bloque'")
            except ValueError:
                os.system("say 'No entendi'")
        elif(entrada[0] == "empezar"): 
            num1 = ''
            num2 = ''
            global start
            
            try:
                if(entrada[1] == "columna" or entrada[1] == "columnas"):
                    num1 = int(entrada[2])
                if(entrada[3] == "fila" or entrada[1] == "filas"):
                    num2 = int(entrada[4])
                if(entrada[3] == "columna" or entrada[1] == "columnas"):
                    num1 = int(entrada[2])
                if(entrada[1] == "fila" or entrada[1] == "filas"):
                    num2 = int(entrada[4])
                if (start != ()):
                    grid[start[0]][start[1]] = 0
                if(num1 != '' and num2 != ''):
                    if (num1 < v_col and num2 < v_fil):
                        os.system("say 'Poniendo punto de inicio'")
                        start = (num2,num1)
                        print("Start: ", start)
                        global grid
                        grid[num2][num1] = 1
                        if(start != () and end != ()):
                            blocks = []
                            limpiar_bloques()
                            blocks = make_blocks() 
                        draw_grid()                      
                    else:
                        os.system("say 'Fuera de rango'")
                else:
                    os.system("say 'No entendi'")
            except ValueError:
                os.system("say 'No entendi'")
        elif(entrada[0] == "fin" or entrada[0] == "sin" ):
            num1 = ''
            num2 = ''
            global end
            try:
                if(entrada[1] == "columna" or entrada[1] == "columnas"):
                    num1 = int(entrada[2])
                if(entrada[3] == "fila" or entrada[1] == "filas"):
                    num2 = int(entrada[4])
                if(entrada[3] == "columna" or entrada[1] == "columnas"):
                    num1 = int(entrada[2])
                if(entrada[1] == "fila" or entrada[1] == "filas"):
                    num2 = int(entrada[4])
                if (end != ()):
                    grid[end[0]][end[1]] = 0
                if(num1 != '' and num2 != ''):
                    if (num1 < v_col and num2 < v_fil):
                        os.system("say 'Poniendo punto de fin'")
                        end = (num2,num1)
                        global grid
                        grid[num2][num1] = 1
                        if(start != () and end != ()):
                            blocks = []
                            limpiar_bloques()
                            blocks = make_blocks()
                        draw_grid()
                    else:
                        os.system("say 'Fuera de rango'")
            except ValueError:
                os.system("say 'No entendi'")
    else:    
        if(entrada[0] == "limpiar"):
            update = True
            print(entrada[0])
            os.system("say 'Limpiando pantalla'")
        if(entrada[0] == "salir"):
            print(entrada[0])
            os.system("say 'Adios mundo cruel'")
            global v_done
            v_done = True
        if(entrada[0] == "correr"):
            global end
            global start
            print("end: ",end,"start: ",start)
            if(end != () and start != ()):
                global start_maze
                start_maze = True
                print(entrada[0])
                os.system("say 'Haciendo el camino'")
            else:
                os.system("say 'Se ocupa un inicio y un fin'")

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


def limpiar_bloques():
    global grid
    global v_fil
    global v_col
    for row in range(v_fil):
        for column in range(v_col):
            if grid[row][column] == 3:
                grid[row][column] = 0
   



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
    if point_end == False and point_start == False:
        grid[row][column] = 1
        start = (row,column)
        point_start = True
    else:
        if point_end == False:
            grid[row][column] = 1
            end = (row,column)
            point_end = True

def bacon_moving(v_margen,path): 
    global v_square 
    Pig = pygame.transform.scale(pygame.image.load("images/pig.png"),(v_square,v_square))
    PigTired = pygame.transform.scale(pygame.image.load("images/pigTired.jpg"),(v_square,v_square))
    for i in path:
        print(i)
        v_len = len(path)-1 
        if(i == path[v_len]):
            window.blit(PigTired, ((v_margen+v_square) * i[1] + v_margen,(v_margen+v_square) * i[0] + v_margen))
            pygame.display.update()
        else:
            window.blit(Pig, ((v_margen+v_square) * i[1] + v_margen,(v_margen+v_square) * i[0] + v_margen))
            pygame.display.update()
        pygame.time.delay(1000)



def make_route(path,blocks):
    global star_board
    global diagonals
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
    global v_fil
    global v_col
    global end
    global start
    global grid
    global blocks
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
    Grass = pygame.transform.scale(pygame.image.load("images//grass.jpg"),(v_square,v_square))
    Stone = pygame.transform.scale(pygame.image.load("images//rock.png"),(v_square,v_square))
    Ground = pygame.transform.scale(pygame.image.load("images//ground.png"),(v_square,v_square))
    Grill = pygame.transform.scale(pygame.image.load("images//grill.jpg"),(v_square,v_square))
    for row in range(0,v_fil):
        for column in range(0,v_col):
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
    global blocks

    global v_done
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

    #Initial and end position 
    in1 = random.randint(0,v_col-1)
    in2 = random.randint(0,v_fil-1)
    start =(in1,in2)
    grid[start[0]][start[1]] = 1
    in1 = random.randint(0,v_col-1)
    in2 = random.randint(0,v_fil-1)
    while(start[0] == in1 and start[1] == in2):
        in1 = random.randint(0,v_col-1)
        in2 = random.randint(0,v_fil-1) 
    end = (in1,in2)
    grid[end[0]][end[1]] = 1

        
    while(v_done == False):
            

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
                make_route(path,blocks) #
                draw_route()
                draw_grid()
                bacon_moving(v_margen,path)
                path = []
                start_maze = False
                end = ()
                start = ()

                               
                      
        clock.tick(60)
        pygame.display.flip()
                

    global escuchando
    escuchando = False
    pygame.quit()


draw()




