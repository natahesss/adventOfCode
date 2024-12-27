from typing import Tuple

from helpers import print_pink, print_green, print_yellow, print_blue

with open('inputs/day10.txt') as inf:
    topographic_map = [list(map(int, list(line.strip()))) for line in inf.readlines()]


counter = 0
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

height = len(topographic_map)
width = len(topographic_map[0])


def find_path(cur_path: Tuple[tuple], history: set, full_path: bool = False):
    cur_path = list(cur_path)
    y, x = cur_path[-1]
    cur_num = topographic_map[y][x]

    if cur_num == 9:  # peak reached
        if full_path:
            history.add(tuple(cur_path))  # count not only peak location, but full unique path
        else:
            history.add((y, x))  # count only peak location
        return cur_path, history

    cross = False
    while not cross:
        next_steps = []

        # checking each possible direction
        for step in steps:
            new_y, new_x = y + step[0], x + step[1]
            if 0 <= new_y < height and 0 <= new_x < width:
                next_num = topographic_map[new_y][new_x]
                if next_num - cur_num == 1:
                    next_steps.append((new_y, new_x))

        # dead end
        if len(next_steps) == 0:
            return cur_path, history

        # only one way - just continue the current path
        if len(next_steps) == 1:
            cur_path.append(next_steps.pop())
            y, x = cur_path[-1]
            cur_num = topographic_map[y][x]

            if cur_num == 9:  # peak reached
                if full_path:
                    history.add(tuple(cur_path))  # count not only peak location, but full unique path
                else:
                    history.add((y, x))  # count only peak location
                return cur_path, history

        # crossroad - more than 1 possible further ways
        else:
            cross = True
            for ns in next_steps:
                new_path = cur_path.copy()
                new_path.append(ns)

                # calling the function recursively for each of the possible ways
                find_path(tuple(new_path), history, full_path=full_path)

    return cur_path, history


s = 0
s2 = 0
for i in range(height):
    for j in range(width):
        if topographic_map[i][j] == 0:
            _, history = find_path(((i, j), ), set())
            s += len(history)

            _, history2 = find_path(((i, j), ), set(), full_path=True)
            s2 += len(history2)


print_pink(f'*** puzzle 1: {s} ***')
print_pink(f'*** puzzle 2: {s2} ***')