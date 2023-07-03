#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def solve_nqueens(n):
    def is_safe(board, row, col):
        """Check if there is a queen in the same column"""
        for i in range(row):
            if board[i] == col:
                return False

        """Check if there is a queen on the upper-left diagonal"""
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i] == j:
                return False

        """Check if there is a queen on the upper-right diagonal"""
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i] == j:
                return False

        return True

    def place_queen(board, row):
        if row == n:
            print_solution(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(board, row + 1)
                board[row] = -1

    def print_solution(board):
        solution = []
        for i in range(n):
            row = ["Q" if board[i] == j else "." for j in range(n)]
            solution.append("".join(row))
        print("\n".join(solution))
        print()

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    place_queen(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
