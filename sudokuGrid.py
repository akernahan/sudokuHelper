SIZE = 9

class SudokuGrid:
    
    def __init__(self, path):
        self.puzzle = path
        self.coord = [0,0]
        self.grid = self.createGrid()
    
    def getX(self):
        return self.coord[0]

    def getY(self):
        return self.coord[1]

    def validRow(self, row, num):
        for i in range(SIZE):
            if self.grid[row][i] == num:
                return False
        return True

    def validColumn(self, col, num):
        for i in range(SIZE):
            if self.grid[i][col] == num:
                return False
        return True

    def validBox(self, row, col, num):
        box_x = int(row/3) * 3
        box_y = int(col/3) * 3
        for i in range(box_x, box_x+3):
            for j in range(box_y, box_y+3):
                if self.grid[i][j] == num:
                    return False
        return True

    def findEmpty(self):
        for x in range(SIZE):
            for y in range(SIZE):
                if self.grid[x][y] == 0:
                    self.coord = [x,y]
                    return True
        return False

    def checkIfSafe(self, num):
        if not self.validRow(self.coord[0], num):
            return False
        if not self.validColumn(self.coord[1], num):
            return False
        if not self.validBox(self.coord[0], self.coord[1], num):
            return False
        return True

    def solveBacktrack(self):
        self.coord = [0,0]

        # find unsolved cell, if there are not any, we have finished
        if not self.findEmpty():
            return True

        row = self.getX()
        column = self.getY()
        # try numbers 1 to 9
        for n in range(1,SIZE+1):
            if self.checkIfSafe(n):
                self.grid[row][column] = n

                if self.solveBacktrack():
                    return True
                
                # reset to 0
                self.grid[row][column] = 0

        return False

    # needs exception handling (probably)
    def createGrid(self):
        with open(self.puzzle, "r") as f:
            t = f.readlines()

        # create a 2D array for the grid
        g = [[0 for x in range(SIZE)]for y in range(SIZE)]
        for x in range(SIZE):
            for y in range(SIZE):
                g[x][y] = int(t[x][y])
        return g
    
    def printGrid(self):
        for i in range(SIZE):
            print(self.grid[i])

if __name__=="__main__":
    g = SudokuGrid("puzzles/Beginner/0.txt")
    g.printGrid()
    if g.solveBacktrack():
        g.printGrid()
    else:
        print("You Failed")
        g.printGrid()
