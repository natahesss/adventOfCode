from math import prod

from helpers import print_pink

with open('inputs/day6.txt') as f:
    lines = [l.strip('\n') for l in f.readlines()]

lines1 = list(
    map(lambda lst: list(
        filter(lambda x: x != '' and x != ' ', lst)),
        map(lambda s: s.split(' '), lines)))

numbers = lines1[:-1]
actions = lines1[-1]


def final_calc(nums: list, act: str) -> int:
    nums = list(map(int, nums))
    if act == '+':
        return sum(nums)
    elif act == '*':
        return prod(nums)
    return 0


max_len = max(map(len, lines[:-1]))
equal_len = list(map(lambda s: s.ljust(max_len, ' '), lines[:-1]))
real_numbers = list(map(''.join, zip(*map(list, equal_len))))

ans1, ans2 = 0, 0
start = 0
for i, action in enumerate(actions):
    n = [lst[i] for lst in numbers]
    ans1 += final_calc(n, action)

    cur_lst = []
    for i in range(start, len(real_numbers)):
        if real_numbers[i].isspace():
            start = i + 1
            break
        cur_lst.append(real_numbers[i])
    ans2 += final_calc(cur_lst, action)

print_pink(f'*** puzzle 1: {ans1} ***')
print_pink(f'*** puzzle 1: {ans2} ***')
