import pygame
from star_algorithm import Node
from star_algorithm import Path
from star_algorithm import Board
from star_algorithm import heuristic
from star_algorithm import setUp
 
#Colors
v_black = (0, 0, 0)
v_white = (255, 255, 255)
v_green = ( 0, 255, 0)
v_red = (255, 0, 0)
v_blue = (0,0,255)
 
#Star algorithm
v_fil = 9
v_col = 12
diagonals = True
end = () 
start = ()

#Screen
v_square  = 50
v_margen = 5
board = []
star_board = []
grid = []
v_dimX = 800
v_dimY = 800
update = False

            
pygame.init()
pantalla = pygame.display.set_mode([v_dimY,v_dimX])
pygame.display.set_caption("speechMaze")
v_done = False 
clock = pygame.time.Clock()

#Initial board
for row in range(v_fil):
    grid.append([])
    for column in range(v_col):
        grid[row].append(0)

for row in range(v_fil):
    for column in range(v_col):
        color = v_white
        pygame.draw.rect(pantalla,
                         color,
                         [(v_margen+v_square) * column + v_margen,
                          (v_margen+v_square) * row + v_margen,
                          v_square,
                          v_square])
pygame.display.flip()



point_end = False
point_start = False
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

        #Update grid with solution
        for row in range(v_fil):
            for column in range(v_col):
                if(star_board.board[row][column].state == "b" ):
                    grid[row][column] = 3
                if(star_board.board[row][column].state == "o" ):
                    grid[row][column] = 2
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
            color = v_white
            if grid[row][column] == 1: #start,end
                color = v_green
            if grid[row][column] == 2: #road
                color = v_blue
            if grid[row][column] == 3: #block
                color = v_black
            pygame.draw.rect(pantalla,
                             color,
                             [(v_margen+v_square) * column + v_margen,
                              (v_margen+v_square) * row + v_margen,
                              v_square,
                              v_square])


                  
    clock.tick(60)
    pygame.display.flip()
            
    

pygame.quit()
