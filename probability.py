#!/usr/bin/env python
import random
import sets

BOARD_SIZE = 9
MINES = 10
SAMPLES = 10**5

def generate_mines(board_size, num_of_mines):
    mines = sets.Set()
    while len(mines) != num_of_mines:
        mines.add((random.randint(0, board_size - 1),
                  random.randint(0, board_size - 1)))
    return mines

def has_adjacent(pos, mines):
    x, y = pos
    if (x + 1, y) in mines:
        return True
    if (x - 1, y) in mines:
        return True
    if (x, y + 1) in mines:
        return True
    if (x, y - 1) in mines:
        return True
    if (x + 1, y + 1) in mines:
        return True
    if (x + 1, y - 1) in mines:
        return True
    if (x - 1, y + 1) in mines:
        return True
    if (x - 1, y - 1) in mines:
        return True
    return False

def random_var_function(mines):
    for mine in mines:
        if not (has_adjacent(mine, mines)):
            return 0
    return 1

print sum([random_var_function(generate_mines(BOARD_SIZE, MINES)) for i in range(0, SAMPLES)]) / float(SAMPLES)

