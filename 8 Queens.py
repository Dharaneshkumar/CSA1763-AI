def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, solutions):
    if row >= len(board):
        solutions.append([''.join(r) for r in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  
            solve_n_queens_util(board, row + 1, solutions)
            board[row][col] = '.'  
def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions
n = 8
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
