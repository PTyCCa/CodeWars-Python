def valid_solution(board):
    """Returns true if valid solution, or false otherwise for 9x9 Sudoku"""
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    
    return not list(filter(lambda x: set(x) != set(range(1, 10)), board + list(zip(*board)) + blocks))


correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def validSolution_2(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False
    
    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False
    
    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            
            if sorted(region) != correct:
                return False
    
    # if everything correct
    return True