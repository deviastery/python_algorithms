def print_board(board):
    for row in board:
        line = ['.' for _ in range(8)]
        line[row] = 'Q'
        print(" ".join(line))
    print()

def is_safe(board, row, col):
    for r, c in enumerate(board[:row]):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_queens(board, row, solution):
    if row == 8:
        print_board(board)
        solution[0] = True
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1, solution)
            if solution[0]:
                return

board = [-1] * 8
solution = [False]
solve_queens(board, 0, solution)
