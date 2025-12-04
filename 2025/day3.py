from typing import Optional

from helpers import print_pink

with open('inputs/day3.txt') as f:
    lines = f.readlines()


def max_digit(lst: list) -> Optional[tuple]:
    for i in range(9, -1, -1):
        try:
            ind = lst.index(i)
            return i, ind
        except ValueError:
            continue


def get_joltage(bank: str, length: int = 2) -> int:
    bank = list(map(int, list(bank)))
    digits = [0] * length
    start_index = 0

    for i in range(length):
        end_index = -(length - 1) + i
        if end_index == 0:
            end_index = len(bank)
        digits[i], found_index = max_digit(bank[start_index:end_index])
        start_index += found_index + 1

    return int(''.join(map(str, digits)))


ans1 = 0
for line in lines:
    res = get_joltage(line.strip())
    ans1 += res

print_pink(f'*** puzzle 1: {ans1} ***')

ans2 = 0
for line in lines:
    res = get_joltage(line.strip(), length=12)
    ans2 += res

print_pink(f'*** puzzle 2: {ans2} ***')
