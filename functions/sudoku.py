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
    
    def mark_errors(self):
        # return 9 lists, one for each row - each list contains those indices there either there is a duplicate in the columns or blocks
        errors = []
        for i in range(9):
            row_errors = []
            for j in range(9):
                if [x[j] for x in self.values].count(self.values[i][j]) > 1:
                    row_errors.append(j)
                block_values = self.values[3*int(i/3)][3*int(j/3):3*(int(j/3) + 1)] + \
                self.values[3*int(i/3) + 1][3*int(j/3):3*(int(j/3) + 1)] + \
                self.values[3*int(i/3) + 2][3*int(j/3):3*(int(j/3) + 1)]
                if block_values.count(self.values[i][j]) > 1:
                    row_errors.append(j)
            errors.append(list(set(row_errors)))
        return errors
