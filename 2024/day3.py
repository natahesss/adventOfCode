import re
from functools import reduce

with open('inputs/day3.txt') as inf:
    data = inf.read()

check_num_length = lambda x: len(x[0]) in range(1, 4) and len(x[1]) in range(1, 4)
multiply = lambda x: int(x[0]) * int(x[1])

pattern = r"mul\(\d+,\d+\)"
ans = reduce(lambda x, y: x+y, map(
    multiply,
    filter(
        check_num_length,
        map(
            lambda x: re.findall(r'\d+', x),
            re.findall(pattern, data)))))
print(f'*** puzzle 1: {ans} ***')

instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data)

enabled = True
ans2 = 0
for instr in instructions:
    if instr.startswith('mul') and enabled:
        a = re.findall(r'\d+', instr)
        if not check_num_length(a):
            continue
        ans2 += multiply(a)
    elif instr == "don't()":
        enabled = False
    elif instr == "do()":
        enabled = True

print(f'*** puzzle 2: {ans2} ***')


