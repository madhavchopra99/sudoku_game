#!/usr/bin/env python
from typing import TypeAlias

board_type: TypeAlias = list[list[int]]
pos_type: TypeAlias = tuple[int, int]

board: board_type = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo: board_type) -> bool:
    '''solves the board and return True if solved'''
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo: board_type, num: int, pos: pos_type) -> bool:
    '''check if the num is valid at position pos = (row,col)'''

    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check region/box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo: board_type) -> None:
    '''print board'''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end="")
    pass


def find_empty(bo: board_type) -> pos_type:
    '''return index for next empty value in format (row,col)'''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row,col

    return False


def main():
    '''main function'''
    global board
    print_board(board)
    solve(board)
    print('_____________________')
    print_board(board)


if __name__ == '__main__':
    main()
