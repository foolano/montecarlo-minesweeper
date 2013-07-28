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
    return sets.Set([(x + 1, y), (x -1, y), (x, y + 1), (x, y -1),
                       (x + 1, y + 1), (x + 1 ,y - 1),
                       (x - 1, y + 1), (x - 1, y - 1)]).intersection(mines)

def random_var_function(mines):
    for mine in mines:
        if not has_adjacent(mine, mines):
            return 0
    return 1

print sum([random_var_function(generate_mines(BOARD_SIZE, MINES)) for i in range(0, SAMPLES)]) / float(SAMPLES)

