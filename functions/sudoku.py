class Sudoku:
    def __init__(self, values):
        self.values = values
        self.cost = self.cost(values)
    
    def count_zeros(self, sudoku):
        count = 0
        for i in range(9): count += sudoku[i].count(0)
        return count
    
    def transpose(self, sudoku):
        trans_sudoku = [[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]]
        for i in range(9):
            for j in range(9):
                trans_sudoku[i][j] = sudoku[j][i]
        return(trans_sudoku)
        
    def cost(self,sudoku):
        penalty = 0
        for i in range(9):
            penalty += 9-len(set(sudoku[i]))
            trans_sudoku = self.transpose(sudoku)
        for i in range(9):
            penalty += 9 - len(set(trans_sudoku[i]))
        for i in range(3):
            for j in range(3):
                values = set()
                for a in range(3):
                    for b in range(3):
                        values.add(sudoku[3*i+a][3*j+b])
                penalty += 9 - len(values)
        return(penalty)
