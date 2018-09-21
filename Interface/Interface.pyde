from star_algorithm import Node
from star_algorithm import Path
from star_algorithm import Board

n = 8
m = 8
diagonals = True
board = []
tablero = []
tam_cuadro = 70
end = (n - 2, m - 2)


def heuristic(node, goal):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    return 10 * (dx + dy) + (14 - 2 * 10) * min(dx, dy)


def make_route():
    star_board = Board(n, m, (1, 1), end, board, [], diagonals)

    # Bloqueos -------------------------

    star_board.setBlock(0, 0)
    star_board.setBlock(5, 0)
    star_board.setBlock(1, 3)
    star_board.setBlock(3, 4)
    star_board.setBlock(4, 2)
    star_board.setBlock(2, 2)
    
    # ----------------------------------
    
    star_board.showBoard()
    
    print("\nStart: ", star_board.start_point)
    print("End: ", star_board.end_point)
    print("Path:")
    while ((star_board.solutionFound == False) or (len(star_board.paths) != 1)):
        star_board.calculatePaths()
        star_board.verifySolution()
        
    for node in star_board.paths[0].pathArray:
        print("Node (", node.i, " , ", node.j,")")
        star_board.board[node.i][node.j].setNodeState("o")
    print(star_board.paths)
    #nd = star_board.paths[0][len(star_board.paths[0].pathArray)-1]
    #star_board.board[nd.i][nd.j].setNodeState("e")

    star_board.showBoard() 
    global tablero
    tablero = star_board
    print(tablero)
    
    
    
def setup():
    size(1000,1000)
    for i in range(0, n):
        temp = []
        for j in range(0, m):
            node = Node(i, j, " ", heuristic((i, j), end))
            temp.append(node)
        board.append(temp)
    make_route()
    


def draw():
    x,y = 50,50
    print(tablero)
    for i in range(0,tablero.n):
        for j in range(0,m):
            if(tablero.board[i][j].state == "s" or tablero.board[i][j].state == "e"):
                fill(255,0,0)
            if(tablero.board[i][j].state == "b" ):
                fill(0,0,0)
            if(tablero.board[i][j].state == "o" ):
                fill(0,0,255) 
            if(tablero.board[i][j].state == " " ):
                fill(255)        
            rect(x,y,tam_cuadro,tam_cuadro)
            x = x + tam_cuadro
        y = y + tam_cuadro
        x = 50
            
    
