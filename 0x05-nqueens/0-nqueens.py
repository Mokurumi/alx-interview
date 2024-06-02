#!/usr/bin/python3
'''
Module that solves the N queens problem
'''


import sys


def is_safe(board, row, col, n):
    '''Check if a queen can be placed in a given position'''
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col, n):
    '''Solve the N queens problem'''
    if col == n:
        print_board(board, n)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0


def print_board(board, n):
    '''Print the board'''
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end=" ")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for j in range(n)] for i in range(n)]
    solve(board, 0, n)
