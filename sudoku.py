import numpy as np


def check_row(value, row):
    return value in row


def check_col(value, grid, col):
    for row in grid:
        if value == row[col]:
            return True


def check_upper_row(value, grid, row, col):
    # Leftmost column
    if ((col + 1) % 3) == 1:
        if value in [grid[row][col + 1], grid[row][col + 2],
                     grid[row + 1][col], grid[row +
                                              1][col + 1], grid[row + 1][col + 2],
                     grid[row + 2][col], grid[row + 2][col+1], grid[row + 2][col + 2]]:
            return True
    # Center column
    elif ((col + 1) % 3) == 2:
        if value in [grid[row][col - 1], grid[row][col + 1],
                     grid[row + 1][col - 1], grid[row +
                                                  1][col], grid[row + 1][col + 1],
                     grid[row + 2][col - 1], grid[row + 2][col], grid[row + 2][col + 1]]:
            return True
    # Rightmost column
    elif ((col + 1) % 3) == 0:
        if value in [grid[row][col - 2], grid[row][col - 1],
                     grid[row + 1][col - 2], grid[row +
                                                  1][col - 1], grid[row + 1][col],
                     grid[row + 2][col - 2], grid[row + 2][col - 1], grid[row + 2][col]]:
            return True


def check_center_row(value, grid, row, col):
    # Leftmost column
    if ((col + 1) % 3) == 1:
        if value in [grid[row - 1][col], grid[row - 1][col + 1], grid[row - 1][col + 2],
                     grid[row][col + 1], grid[row][col + 2],
                     grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2]]:
            return True
    # Center column
    elif ((col + 1) % 3) == 2:
        if value in [grid[row - 1][col - 1], grid[row - 1][col], grid[row - 1][col + 1],
                     grid[row][col - 1], grid[row][col + 1],
                     grid[row + 1][col - 1], grid[row + 1][col], grid[row + 1][col + 1]]:
            return True
    # Rightmost column
    elif ((col + 1) % 3) == 0:
        if value in [grid[row - 1][col - 2], grid[row - 1][col - 1], grid[row - 1][col],
                     grid[row][col - 2], grid[row][col - 1],
                     grid[row + 1][col - 2], grid[row + 1][col - 1], grid[row + 1][col]]:
            return True


def check_bottom_row(value, grid, row, col):
    # Leftmost column
    if ((col + 1) % 3) == 1:
        if value in [grid[row - 2][col], grid[row - 2][col + 1], grid[row - 2][col + 2],
                     grid[row - 1][col], grid[row -
                                              1][col + 1], grid[row - 1][col + 2],
                     grid[row][col + 1], grid[row][col + 2]]:
            return True
    # Center column
    elif ((col + 1) % 3) == 2:
        if value in [grid[row - 2][col - 1], grid[row - 2][col], grid[row - 2][col + 1],
                     grid[row - 1][col - 1], grid[row -
                                                  1][col], grid[row - 1][col + 1],
                     grid[row][col - 1], grid[row][col + 1]]:
            return True
    # Rightmost column
    elif ((col + 1) % 3) == 0:
        if value in [grid[row - 2][col - 2], grid[row - 2][col - 1], grid[row - 2][col],
                     grid[row - 1][col - 2], grid[row -
                                                  1][col - 1], grid[row - 1][col],
                     grid[row][col - 2], grid[row][col - 1]]:
            return True


def check_box(value, grid, row, col):
    if ((row + 1) % 3) == 1:  # Upper row of each box
        return check_upper_row(value, grid, row, col)
    elif ((row + 1) % 3) == 2:  # Center row of each box
        return check_center_row(value, grid, row, col)
    elif ((row + 1) % 3) == 0:  # Bottom row of each box
        return check_bottom_row(value, grid, row, col)


def create_grid(max_clues):
    grid = np.zeros((9, 9), dtype=int)
    mem = []

    while max_clues != 0:
        new_i = np.random.randint(0, 9)
        new_j = np.random.randint(0, 9)

        i_j = [new_i, new_j]

        if i_j in mem:
            continue

        mem.append(i_j)

        new_clue = np.random.randint(1, 10)

        if grid[new_i][new_j] == 0:
            if not((check_row(new_clue, grid[new_i])) or
                   (check_col(new_clue, grid, new_j)) or
                   (check_box(new_clue, grid, new_i, new_j))):
                grid[new_i][new_j] = new_clue
                max_clues -= 1

    return grid


def print_grid(grid):
    for row in range(len(grid)):
        for j in range(len(grid[row])):
            if (((j + 1) % 3) == 0) and ((j + 1) != len(grid[row])):
                print(f' {grid[row][j]} |', end='')
            else:
                print(f' {grid[row][j] }', end='')
        if (((row + 1) % 3) == 0) and ((row + 1) != len(grid)):
            print('\n-----------------------')
        else:
            print('')


max_clues = np.random.randint(17, 33)

grid = create_grid(max_clues)

print_grid(grid)
