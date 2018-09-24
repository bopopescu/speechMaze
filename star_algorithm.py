'''
Algoritmo Estrella
'''

import random

def heuristic(node, goal):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    return 10 * (dx + dy) + (14 - 2 * 10) * min(dx, dy)


    

def setUp(n,m,start,end,board,diagonals):
    star_board = Board(n, m,start, end, board, [], diagonals)

    # Bloqueos -------------------------
    for i in range(n):
        for j in range(m):
            ran = random.randint(1,100)
            if(ran < 20):
                star_board.setBlock(i,j)
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
    return star_board

class Board:

    def __init__(self, n, m, start_point, end_point, board, paths, diagonals):
        self.n = n
        self.m = m
        self.start_point = start_point
        self.end_point = end_point
        self.board = board
        self.paths = paths
        self.diagonals = diagonals
        if start_point != () and end_point != ():
            self.board[start_point[0]][start_point[1]].setNodeState("s")
            self.board[end_point[0]][end_point[1]].setNodeState("e")
        self.solutionFound = False

    def showBoard(self):
        print("  " + (" --- " * self.m))
        for i in range(0, self.n):
            row = ""
            for j in range(0, self.m):
                if (j == 0):
                    row += str(i)
                    row += " | "    
                else:
                    row += "| "
                row += str(self.board[i][j].state)
                row += " |"
            print(row)
            print("  " + (" --- " * self.m))
        last_row = "    "
        for i in range(0, self.m):
            last_row += (str(i) + "    ")
        print(last_row)


    def setBlock(self, row_position, column_position):
        self.board[row_position][column_position].setNodeState("b")

    def verifySolution(self):
        if self.solutionFound == False:
            for path in self.paths:
                if (path.actualPosition == self.end_point):
                    self.solutionFound = True
                    
        if self.solutionFound == True:
            bestSolution = self.paths[0]
            for path in self.paths:
                if (path.actualPosition == self.end_point):
                    bestSolution = path
            for path in self.paths:
                if (path.actualPosition == self.end_point):
                    if (path.pathCost < bestSolution.pathCost):
                        bestSolution = path
            pathsToRemove = []
            for path in self.paths:
                if (path.pathCost >= bestSolution.pathCost and path != bestSolution):
                    pathsToRemove.append(path)
            for path in pathsToRemove:
                self.paths.remove(path)
            
        

    def calculatePaths(self):
        if (len(self.paths) == 0):
            p = Path(self.start_point, 0, 0, [])
            self.paths.append(p)
        else:
            p = self.paths[0]
            for path in self.paths:
                if (path.pathCost < p.pathCost):
                    if (path.actualPosition != self.end_point):
                        p = path
            if (p.actualPosition != self.end_point):
                temp = self.expandPath(p)
            self.paths.remove(p)
            for path in temp:
                self.paths.append(path)
            '''
            print("Round -------------------------------------")
            for path in self.paths:
                t = "["
                for node in path.pathArray:
                    t += "("
                    t += str(node.i)
                    t += ", "
                    t += str(node.j)
                    t += "), "
                t += ("h(n): " + str(node.heuristic) + " --- " + str(heuristic((node.i, node.j), self.end_point)))
                t += "]"
                print(t)
            '''
            
    def expandPath(self, path):
        tempPaths = []
        # Right border limit
        if (path.actualPosition[1] < (self.m - 1)):
            p1_i = path.actualPosition[0]
            p1_j = path.actualPosition[1] + 1
            if (self.board[p1_i][p1_j].state != "b"):
                p1 = self.expand_right(path, p1_i, p1_j)
                tempPaths.append(p1)
        # Left border limit
        if (path.actualPosition[1] > 0):
            p2_i = path.actualPosition[0]
            p2_j = path.actualPosition[1] - 1
            if (self.board[p2_i][p2_j].state != "b"):
                p2 = self.expand_left(path, p2_i, p2_j)
                tempPaths.append(p2)
        # Up border limit
        if (path.actualPosition[0] > 0):
            p3_i = path.actualPosition[0] - 1
            p3_j = path.actualPosition[1]
            if (self.board[p3_i][p3_j].state != "b"):
                p3 = self.expand_up(path, p3_i, p3_j)
                tempPaths.append(p3)
        # Down border limit
        if (path.actualPosition[0] < (self.n - 1)):
            p4_i = path.actualPosition[0] + 1
            p4_j = path.actualPosition[1]
            if (self.board[p4_i][p4_j].state != "b"):
                p4 = self.expand_down(path, p4_i, p4_j)
                tempPaths.append(p4)
        if (self.diagonals == True):
            # UpRight border limit
            if ((path.actualPosition[1] < (self.m - 1)) and (path.actualPosition[0] > 0)):
                p5_i = path.actualPosition[0] - 1
                p5_j = path.actualPosition[1] + 1
                if (self.board[p5_i][p5_j].state != "b"):
                    if ((self.board[p5_i][p5_j - 1].state != "b") or (self.board[p5_i + 1][p5_j].state != "b")):
                        p5 = self.expand_upRight(path, p5_i, p5_j)
                        tempPaths.append(p5)
            # UpLeft border limit
            if ((path.actualPosition[1] > 0) and (path.actualPosition[0] > 0)):
                p6_i = path.actualPosition[0] - 1
                p6_j = path.actualPosition[1] - 1
                if (self.board[p6_i][p6_j].state != "b"):
                    if ((self.board[p6_i][p6_j + 1].state != "b") or (self.board[p6_i + 1][p6_j].state != "b")):
                        p6 = self.expand_upLeft(path, p6_i, p6_j)
                        tempPaths.append(p6)
            # DownRight border limit
            if ((path.actualPosition[1] < (self.m - 1)) and (path.actualPosition[0] < (self.n - 1))):
                p7_i = path.actualPosition[0] + 1
                p7_j = path.actualPosition[1] + 1
                if (self.board[p7_i][p7_j].state != "b"):
                    if ((self.board[p7_i][p7_j - 1].state != "b") or (self.board[p7_i - 1][p7_j].state != "b")):
                        p7 = self.expand_downRight(path, p7_i, p7_j)
                        tempPaths.append(p7)
            # DownLeft border limit
            if ((path.actualPosition[1] > 0) and (path.actualPosition[0] < (self.n - 1))):
                p8_i = path.actualPosition[0] + 1
                p8_j = path.actualPosition[1] - 1
                if (self.board[p8_i][p8_j].state != "b"):
                    if ((self.board[p8_i][p8_j + 1].state != "b") or (self.board[p8_i - 1][p8_j].state != "b")):
                        p8 = self.expand_downLeft(path, p8_i, p8_j)
                        tempPaths.append(p8)
        return tempPaths
        

    def expand_right(self, path, p1_i, p1_j):
        # Right movement
        p1_gCost = path.gCost + 10
        p1_pathCost = p1_gCost + self.board[p1_i][p1_j].heuristic
        p1_array = []
        for i in path.pathArray:
            p1_array.append(i)
        p1_array.append(self.board[p1_i][p1_j])
        p1 = Path((p1_i, p1_j), p1_gCost, p1_pathCost, p1_array)
        return p1

    def expand_left(self, path, p2_i, p2_j):
        # Left movement
        p2_gCost = path.gCost + 10
        p2_pathCost = p2_gCost + self.board[p2_i][p2_j].heuristic
        p2_array = []
        for i in path.pathArray:
            p2_array.append(i)
        p2_array.append(self.board[p2_i][p2_j])
        p2 = Path((p2_i, p2_j), p2_gCost, p2_pathCost, p2_array)
        return p2

    def expand_up(self, path, p3_i, p3_j):
        # Up movement
        p3_gCost = path.gCost + 10
        p3_pathCost = p3_gCost + self.board[p3_i][p3_j].heuristic
        p3_array = []
        for i in path.pathArray:
            p3_array.append(i)
        p3_array.append(self.board[p3_i][p3_j])
        p3 = Path((p3_i, p3_j), p3_gCost, p3_pathCost, p3_array)
        return p3

    def expand_down(self, path, p4_i, p4_j):
        # Down movement
        p4_gCost = path.gCost + 10
        p4_pathCost = p4_gCost + self.board[p4_i][p4_j].heuristic
        p4_array = []
        for i in path.pathArray:
            p4_array.append(i)
        p4_array.append(self.board[p4_i][p4_j])
        p4 = Path((p4_i, p4_j), p4_gCost, p4_pathCost, p4_array)
        return p4

    def expand_upRight(self, path, p5_i, p5_j):
        # Up-Right movement
        p5_gCost = path.gCost + 14
        p5_pathCost = p5_gCost + self.board[p5_i][p5_j].heuristic
        p5_array = []
        for i in path.pathArray:
            p5_array.append(i)
        p5_array.append(self.board[p5_i][p5_j])
        p5 = Path((p5_i, p5_j), p5_gCost, p5_pathCost, p5_array)
        return p5

    def expand_upLeft(self, path, p6_i, p6_j):
        # Up-Left movement
        p6_gCost = path.gCost + 14
        p6_pathCost = p6_gCost + self.board[p6_i][p6_j].heuristic
        p6_array = []
        for i in path.pathArray:
            p6_array.append(i)
        p6_array.append(self.board[p6_i][p6_j])
        p6 = Path((p6_i, p6_j), p6_gCost, p6_pathCost, p6_array)
        return p6

    def expand_downRight(self, path, p7_i, p7_j):
        # Down-Right movement
        p7_gCost = path.gCost + 14
        p7_pathCost = p7_gCost + self.board[p7_i][p7_j].heuristic
        p7_array = []
        for i in path.pathArray:
            p7_array.append(i)
        p7_array.append(self.board[p7_i][p7_j])
        p7 = Path((p7_i, p7_j), p7_gCost, p7_pathCost, p7_array)
        return p7

    def expand_downLeft(self, path, p8_i, p8_j):
        # Down-Left movement
        p8_gCost = path.gCost + 14
        p8_pathCost = p8_gCost + self.board[p8_i][p8_j].heuristic
        p8_array = []
        for i in path.pathArray:
            p8_array.append(i)
        p8_array.append(self.board[p8_i][p8_j])
        p8 = Path((p8_i, p8_j), p8_gCost, p8_pathCost, p8_array)
        return p8

        
                
        

class Node:
    
    def __init__(self, i, j, state, heuristic):
        self.i = i
        self.j = j
        self.heuristic = heuristic
        self.state = state
        self.value = ""
        
    def setNodeValue(self, value):
        self.value = value

    def setNodeState(self, state):
        self.state = state


class Path:

    def __init__(self, actualPosition, gCost, pathCost, pathArray):
        self.actualPosition = actualPosition
        self.gCost = gCost
        self.pathCost = pathCost
        self.pathArray = pathArray

    def addNode(self, node):
        self.pathArray.append(node)
        
