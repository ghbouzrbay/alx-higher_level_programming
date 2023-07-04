#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys

def is_valid(board, row, col):
    """Check if placing a queen at a given position is valid."""
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    """Solve the N Queens problem and print all solutions."""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[' ' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    
    for solution in solutions:
        print(solution)


def backtrack(board, row, solutions):
    """Backtracking algorithm to solve the N Queens problem."""
    if row == len(board):
        solutions.append(get_solution(board))
        return
    
    n = len(board)
    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = ' '


def get_solution(board):
    """Convert the board to the list of queen positions."""
    n = len(board)
    solution = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'Q':
                solution.append([row, col])
    return solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
