#!/usr/bin/python3
'''
Module that solves the N queens problem
'''


import sys


def is_safe(board, row, col, n):
    '''
    Determines if a queen can be placed on board at row, col
    '''
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


def print_solutions(board):
    '''
    Prints the solutions to the N queens problem
    '''
    n = len(board)
    solutions = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solutions.append([i, j])
    print(solutions)


def backtrack(board, col, n):
    '''
    Backtracking function to solve N queens problem
    '''
    if col == n:
        print_solutions(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = backtrack(board, col + 1, n) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    '''
    Solves the N queens problem
    '''
    board = [[0 for j in range(n)] for i in range(n)]
    if not backtrack(board, 0, n):
        print("Solution does not exist")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
