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

def make_step(coords: tuple, step: tuple, left: bool = True, inverted_diag: bool = False) -> tuple:
    if left:
        return coords[0] - step(0), coords[1] + step[1] * (-1 + 2 * inverted_diag)

def check_antinode_fits_borders(antinode: tuple) -> bool:
    return 0 <= antinode[0] < height and 0 <= antinode[1] < width


def calculate_antinode(one: tuple, two: tuple, to_borders: bool = False) -> set:
    one, two = sorted([one, two])

    y1, x1 = one
    y2, x2 = two

    y_diff = y1 - y2
    x_diff = x1 - x2

    res = set()
    if y_diff <= 0 and x_diff <= 0:
        left, right = ((y1 - abs(y_diff), x1 - abs(x_diff)), (y2 + abs(y_diff), x2 + abs(x_diff)))
        res.update([left, right])
    else:
        left, right = ((y1 - abs(y_diff), x1 + abs(x_diff)), (y2 + abs(y_diff), x2 - abs(x_diff)))
        res.update([left, right])
    return res


final = set()
for k, v in antennas_cords.items():
    for opt in combinations(v, 2):
        new_atinodes = calculate_antinode(*opt)
        new_atinodes = list(filter(check_antinode_fits_borders, new_atinodes))
        final.update(new_atinodes)

print(sorted(final))
print_pink(f"*** puzzle 1: {len(final)} ***")
# [(0, 6), (0, 11), (1, 3), (2, 4), (2, 10), (3, 2), (4, 9), (5, 1), (5, 6), (6, 3), (7, 0), (7, 7), (10, 10), (11, 10)]

final2 = set()
# for k, v in antennas_cords.items():
#     print_pink(f"*** {k} ***")
#     for opt in combinations(v, 2):
#         print_blue(opt)
#         new_atinodes = calculate_antinode(*opt, to_borders=True)
#         print('new:', len(new_atinodes), new_atinodes)
#         new_atinodes = list(filter(check_antinode_fits_borders, new_atinodes))
#         print('filtered', len(new_atinodes), new_atinodes)
#         final2.update(new_atinodes)


print_pink(f"*** puzzle 2: {len(final2)} ***")
# 1125 - too low
