SIZE = 9

class SudokuGrid:
    
    def __init__(self, path):
        self.puzzle = path
        self.grid = self.createGrid()
    
    def valid_row(self, row, num):
        for i in range(SIZE):
            if self.grid[row][i] == num:
                return False
        return True

    def valid_column(self, col, num):
        for i in range(SIZE):
            if self.grid[i][col] == num:
                return False
        return True

    # unsure if this works
    def valid_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.grid[int(row/3)+i][int(col/3)+j] == num:
                    return False
        return True

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
    g = SudokuGrid("puzzles/Master/0.txt")
    g.printGrid()