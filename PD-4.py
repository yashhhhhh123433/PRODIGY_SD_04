def is_valid(board, row, col, num):
    # Check if the number is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell (denoted by 0) in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None  # If no empty cell is found, puzzle is solved

def solve_sudoku(board):
    # Find an empty location
    row, col = find_empty_location(board)

    # If no empty cell is found, the puzzle is solved
    if row is None or col is None:
        return True

    # Try placing a number (1 to 9) in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the placement is valid, update the board and continue solving
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If the recursion leads to a solution, return True

            # If the placement leads to an invalid solution, backtrack
            board[row][col] = 0

    return False  # No valid number can be placed, trigger backtracking

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    # Input unsolved Sudoku puzzle as a 2D list
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        print_sudoku(puzzle)
    else:
        print("No solution exists.")
