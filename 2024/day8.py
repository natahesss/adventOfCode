from itertools import combinations
from typing import Optional, Union

from helpers import print_pink, print_blue

with open('inputs/day.txt') as inf:
    data = [line.strip() for line in inf.readlines()]

height = len(data)
width = len(data[0])

antennas_cords = dict()
for i in range(height):
    for j in range(width):
        if data[i][j] != '.':
            antennas_cords.setdefault(data[i][j], []).append((i, j))

# print(antennas_cords)

def check_antinode_fits_borders(antinode: tuple) -> bool:
    return 0 <= antinode[0] < height and 0 <= antinode[1] < width


def calculate_antinode(one: tuple, two: tuple, to_borders: bool = False) -> list:
    one, two = sorted([one, two])

    y1, x1 = one
    y2, x2 = two

    y_diff = y1 - y2
    x_diff = x1 - x2

    res = []
    if y_diff <= 0 and x_diff <= 0:
        print_pink('normal diagonal')
        left, right = ((y1 - abs(y_diff), x1 - abs(x_diff)), (y2 + abs(y_diff), x2 + abs(x_diff)))
        if to_borders:
            if check_antinode_fits_borders(left):
                go_left, go_right = left, left
            elif check_antinode_fits_borders(right):
                go_left, go_right = right, right
            else:
                return []
            while check_antinode_fits_borders(go_left):
                print(f'left is correct: {go_left}')
                res.append(left)
                left = (left[0] - abs(y_diff), left[1] - abs(x_diff))
            while check_antinode_fits_borders(right):
                print(f'right is correct: {right}')
                res.append(right)
                right = (right[0] + abs(y_diff), right[1] + abs(x_diff))
        else:
            res.extend([left, right])
    else:
        print_pink('inverted diagonal')
        left, right = ((y1 - abs(y_diff), x1 + abs(x_diff)), (y2 + abs(y_diff), x2 - abs(x_diff)))
        if to_borders:
            while check_antinode_fits_borders(left):
                print(f'left is correct: {left}')
                res.append(left)
                left = (left[0] - abs(y_diff), left[1] + abs(x_diff))
            while check_antinode_fits_borders(right):
                print(f'right is correct: {right}')
                res.append(right)
                right = (right[0] + abs(y_diff), right[1] - abs(x_diff))
        else:
            res.extend([left, right])
    return res



final = set()
for k, v in antennas_cords.items():
    for opt in combinations(v, 2):
        new_atinodes = calculate_antinode(*opt)
        new_atinodes = list(filter(check_antinode_fits_borders, new_atinodes))
        final.update(new_atinodes)

print_pink(f"*** puzzle 1: {len(final)} ***")

final2 = set()
for k, v in antennas_cords.items():
    print_pink(f"*** {k} ***")
    for opt in combinations(v, 2):
        print_blue(opt)
        new_atinodes = calculate_antinode(*opt, to_borders=True)
        print('new:', len(new_atinodes), new_atinodes)
        new_atinodes = list(filter(check_antinode_fits_borders, new_atinodes))
        print('filtered', len(new_atinodes), new_atinodes)
        final2.update(new_atinodes)

print_pink(f"*** puzzle 2: {len(final2)} ***")
