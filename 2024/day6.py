import time

from typing import Union

from helpers import print_pink

def print_matrix(matrix: list):
    for line in matrix:
        print(''.join(line))

with open('inputs/day6.txt') as inf:
    matrix = [list(line.strip()) for line in inf.readlines()]

width = len(matrix[0])
height = len(matrix)

for i in range(height):
    if '^' in matrix[i]:
        start = [i, matrix[i].index('^')]
        matrix[i][start[1]] = 'X'
        break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_path(mx: list, start: Union[list, tuple]):
    mx = [item.copy() for item in mx]
    current_dir = 0
    position = start
    while True:
        # possible next step forward
        new_i, new_j = position[0] + directions[current_dir][0], position[1] + directions[current_dir][1]

        # check borders
        if new_i >= height or new_i < 0 or new_j >= width or new_j < 0:
            break

        # step forward if possible
        if mx[new_i][new_j] in ('X', '.'):
            position = [new_i, new_j]
            mx[new_i][new_j] = 'X'
            continue
        # change direction if obstacle
        elif mx[new_i][new_j] == '#':
            current_dir = (current_dir + 1) % 4

    return mx

matrix_with_path = get_path(matrix, start)
print_matrix(matrix_with_path)

ans1 = sum(map(lambda x: x.count('X'), matrix_with_path))

print_pink(f"*** puzzle 1: {ans1} ***")

# puzzle 2
# NOT OPTIMIZED AT ALL...

def check_loop_exists(mx: list, new_obst: Union[list, tuple], start_pos: Union[list, tuple]) -> bool:
    mx = [item.copy() for item in mx]
    position = list(start_pos)
    mx[new_obst[0]][new_obst[1]] = '0'

    turns = []
    turns_count = dict()

    current_dir = 0
    # print_pink(f"new_obst: {new_obst}")
    while True:
        # possible next step forward
        new_i, new_j = position[0] + directions[current_dir][0], position[1] + directions[current_dir][1]

        # check borders
        if new_i >= height or new_i < 0 or new_j >= width or new_j < 0:
            # print_matrix(mx)
            return False

        # step forward if possible
        if mx[new_i][new_j] in ('X', '.', '+'):
            if mx[new_i][new_j] == '.':
                mx[new_i][new_j] = 'X'
            position = [new_i, new_j]
            continue
        # change direction if obstacle
        elif mx[new_i][new_j] in ('#', '0'):
            mx[position[0]][position[1]] = '+'

            position_tuple = tuple(position)
            turns.append(position_tuple)
            turns_count.setdefault(position_tuple, 0)
            turns_count[position_tuple] += 1
            # print(turns)
            # cur_turn_count = turns.count(position)
            # print(cur_turn_count)
            if turns_count[position_tuple] >= 2:
                if turns[-1] != turns[-2]:
                    # prev_turn_count = turns.count(turns[-2])
                    # print(prev_turn_count)
                    if turns_count[turns[-2]] >= 2:
                        # print_matrix(mx)
                        return True
            current_dir = (current_dir + 1) % 4

start_time = time.time()
answers = []
for i in range(height):
    for j in range(width):
        if matrix[i][j] == '.':
            if check_loop_exists(matrix, (i, j), start):
                answers.append([i, j])
end_time = time.time()

print(f"Execution time: {end_time - start_time}")
print_pink(f"*** puzzle 2: {len(answers)} ***")
