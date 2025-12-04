from helpers import print_pink

with open('inputs/day1.txt') as f:
    lines = f.readlines()

start = 50


def move_dial(position: int, instruction: str) -> int:
    step = int(instruction[1:])
    res = (position + (-1 if instruction.lower().startswith('l') else 1) * step) % 100

    if res < 0:
        res = 99 - res
    return res


ans1 = 0
for line in lines:
    res = move_dial(start, line)
    if res == 0:
        ans1 += 1
    start = res

print_pink(f'*** puzzle 1: {ans1} ***')

# part 2
start = 50
ans2 = 0


def move_dial_and_count_zeros(position: int, instruction: str) -> tuple:
    step = int(instruction[1:])
    if step == 0:
        return start, 0
    is_negative = instruction.lower().startswith('l')
    res = position + (-1 if is_negative else 1) * step

    zeros = abs(res) // 100
    if res <= 0:
        if start != 0:
            zeros += 1

    res = res % 100
    if res < 0:
        res = 99 - res

    return res, zeros


for line in lines:
    res, zeros = move_dial_and_count_zeros(start, line)
    start = res
    ans2 += zeros

print_pink(f'*** puzzle 2: {ans2} ***')
