#!/usr/bin/env python
import random
import sets

BOARD_SIZE = 9
MINES = 10
SAMPLES = 10**6

def generate_mines(board_size, num_of_mines):
    return [(i / BOARD_SIZE, i % BOARD_SIZE) for i in random.sample(range(0, BOARD_SIZE**2), MINES)]

def adjacents(pos, mines):
    rg = range(-1, 2)
    return sets.Set([(pos[0] + i, pos[1] + j) for i in rg for j in rg if (i or j)]).intersection(mines)

def random_var_function(mines):
    can_reach = adjacents(mines.pop(), mines)
    while can_reach:
        pos = can_reach.pop()
        if pos in mines:
            mines.remove(pos)
            can_reach = can_reach.union(adjacents(pos, mines))
    return int(not bool(mines))

print sum([random_var_function(generate_mines(BOARD_SIZE, MINES)) for i in xrange(0, SAMPLES)]) / float(SAMPLES)
