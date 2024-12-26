from functools import reduce
from itertools import chain

from helpers import print_pink, print_blue, print_green

with open('inputs/day9.txt') as inf:
    init_data = list(map(int, inf.read().strip()))

# even - data
# odd - empty space

def compress_data_alg1(data: list) -> list:
    data_map = []

    last_data_index = len(data) - 1 - (len(data) % 2 == 0)
    c = 0 # file ID number counter
    for i in range(len(data)):
        # adding data to the resulting map
        if i % 2 == 0:
            data_map.extend([c] * data[i])
            c += 1
        else:
            # filling up the empty space with last files
            for j in range(data[i]):

                # searching for non-empty files in the end of the files list
                last_file = data[last_data_index]
                while last_file == 0:
                    last_data_index -= 2
                    last_file = data[last_data_index]

                # adding found block to the map
                data_map.append(last_data_index // 2)

                # decreasing number of blocks in the last file
                data[last_data_index] -= 1

        # iterating from both ends met
        if last_data_index == i:
            break

    return data_map

def calc_check_sum(lst: list) -> int:
    return reduce(lambda a, b: a + b, map(lambda x: x[0] * x[1], enumerate(lst)))

map1 = compress_data_alg1(init_data.copy())

print_pink(f'*** puzzle 1: {calc_check_sum(map1)} ***')


def compress_data_alg2(data: list) -> list:
    data_copy = data.copy()
    data_map = []

    last_data_index = len(data) - 1 - (len(data) % 2 == 0)
    c = 0  # file ID number counter
    for i in range(len(data)):
        # adding data to the resulting map
        if i % 2 == 0:

            if data[i] == 0:
                # file was already moved to the empty space
                file = [0] * data_copy[i]
            else:
                # file is not moved yet and has some data
                file = [c] * data[i]

            data_map.append(file)
            c += 1
        else:
            empty_space = data[i]

            if empty_space == 0:
                continue

            reorganized_empty_space = []

            # moving starting point for backwards search
            if data[last_data_index] == 0:
                last_data_index -= 2

            for j in range(last_data_index, i, -2):
                # searching for non-empty files in the end of the files list that will fit the empty space
                last_file = data[j]
                if last_file == 0: # empty file
                    continue
                if last_file > empty_space: # too large file
                    continue

                reorganized_empty_space.extend([j // 2] * last_file) # filling u the empty space
                data[j] = 0 # removing moved file from the initial list
                empty_space -= last_file
                if empty_space == 0: # empty space is filled
                    break
                if i == j:
                    break

            if empty_space > 0:
                reorganized_empty_space.extend([0] * empty_space) # filling up the rest of the empty space with zeros
            data_map.append(reorganized_empty_space)

    return data_map

map2 = compress_data_alg2(init_data.copy())

print_pink(f'*** puzzle 2: {calc_check_sum(chain.from_iterable(map2))} ***')


