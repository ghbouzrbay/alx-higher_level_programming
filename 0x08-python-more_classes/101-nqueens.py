#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    board = []
    for _ in range(n):
        row = [' '] * n
        board.append(row)
    return board


def board_deepcopy(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board

def get_solution(board):
    """Return a list of queen positions in a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def xout(board, row, col):
    """Mark out spots on the chessboard where non-attacking queens cannot be placed.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(board)

    # X out all spots horizontally and vertically
    for i in range(n):
        board[row][i] = "x"
        board[i][col] = "x"

    # X out all spots diagonally
    for i in range(n):
        for j in range(n):
            if i + j == row + col or i - j == row - col:
                board[i][j] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    
    Returns:
        solutions (list): The updated list of solutions.
    """
    n = len(board)

    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == " ":
            new_board = board_deepcopy(board)
            new_board[row][col] = "Q"
            xout(new_board, row, col)
            solutions = recursive_solve(new_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    chessboard = init_board(N)
    solutions = recursive_solve(chessboard, 0, 0, [])
    
    for sol in solutions:
        print(sol)
