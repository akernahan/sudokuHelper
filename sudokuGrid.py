class SudokuGrid:
    
    def __init__(self, path):
        self.puzzle = path
        self.grid = self.createGrid()
    
    def createGrid(self):
        b = [[0,4,0,0,5,0,0,0,0],
            [2,0,0,0,0,7,0,5,3],
            [0,0,3,0,0,0,0,0,6],
            [0,0,0,7,0,0,0,9,0],
            [0,0,6,4,8,5,2,0,0],
            [0,3,0,0,0,1,0,0,0],
            [8,0,0,0,0,0,7,0,0],
            [3,5,0,2,0,0,0,0,4],
            [0,0,0,0,9,0,0,2,0]]
        return b