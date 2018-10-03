import pygame
from star_algorithm import Node
from star_algorithm import Path
from star_algorithm import Board
from star_algorithm import heuristic
from star_algorithm import setUp

 
#Star algorithm
v_fil = 8
v_col = 8
v_square  = 50
diagonals = True
end = () 
start = ()
update = False

#Grid variables
grid = []
point_end = False
point_start = False
v_margen = 5

#Images
Grass = pygame.transform.scale(pygame.image.load("images\\grass.jpg"),(v_square,v_square))
Stone = pygame.transform.scale(pygame.image.load("images\\rock.png"),(v_square,v_square))
Ground = pygame.transform.scale(pygame.image.load("images\\ground.png"),(v_square,v_square))
Wood = pygame.transform.scale(pygame.image.load("images\\wood.png"),(v_square,v_square))
Grill = pygame.transform.scale(pygame.image.load("images\\grill.jpg"),(v_square,v_square))
Pig = pygame.transform.scale(pygame.image.load("images\\pig.png"),(v_square,v_square))
PigTired = pygame.transform.scale(pygame.image.load("images\\pigTired.jpg"),(v_square,v_square))
    

    

        
pygame.init()
window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
pygame.display.set_caption("speechMaze")
 
clock = pygame.time.Clock()



def reload_grid():
    global grid
    global window
    global point_end
    global point_start
    grid = []
    for row in range(v_fil):
        grid.append([])
        for column in range(v_col):
            grid[row].append(0)
    point_end = False
    point_start = False


def update_col(col):
    global v_col
    global v_fil
    global v_square
    v_col = col
    window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
    reload_grid() 

def update_fil(fil):
    global v_col
    global v_fil
    global v_square
    v_fil = fil
    window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
    reload_grid()
    

def update_tam(tam):
    global v_col
    global v_fil
    global v_square
    v_square = tam
    window = pygame.display.set_mode([(v_col+1)*v_square,(v_fil+1)*v_square])
    reload_grid()

    

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


def make_route(path):
    global grid
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


def draw():
    global end
    global start
    global v_fil
    global v_col
    global grid
    global point_start
    global point_end
    global v_margen

    v_done = False
    path = []
    board = []
    star_board = []

    #Initial board
    for row in range(v_fil):
        grid.append([])
        for column in range(v_col):
            grid[row].append(0)

        
    while not v_done:

        #Make route with star algorith
        if end != () and start != ():
            make_route(path)
            end = ()
            start = ()                    

            
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


            for row in range(v_fil):
                for column in range(v_col):
                    window.blit(Grass, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 1: #start,end
                        window.blit(Ground, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 2: #road
                        window.blit(Grill, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))
                    if grid[row][column] == 3: #block
                        window.blit(Stone, ((v_margen+v_square) * column + v_margen,(v_margen+v_square) * row + v_margen))

            #simulate pig walking
            if path != []:
                bacon_moving(v_margen,v_square,path)
                path = []

                               
                      
        clock.tick(60)
        pygame.display.flip()
                
        
    pygame.quit()


draw()
