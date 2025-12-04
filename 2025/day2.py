from helpers import print_pink

with open('inputs/day2.txt') as f:
    ids = list(map(lambda x: x.strip().lstrip('0'), f.read().split(',')))


def is_id_invalid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    return s[0:len(s) // 2] == s[len(s) // 2:]


def check_id_range(inp: str, validator) -> int:
    start, end = inp.split('-')
    s = 0
    for i in range(int(start), int(end) + 1):
        if validator(str(i)):
            s += i
    return s


ans1 = 0
for item in ids:
    ans1 += check_id_range(item, is_id_invalid)

print_pink(f'*** puzzle 1: {ans1} ***')


def is_id_invalid_improved(s: str) -> bool:
    length = len(s) // 2
    for i in range(length, 0, -1):
        if s[:i] * (len(s) // i) == s:
            return True
    return False


ans2 = 0
for item in ids:
    ans2 += check_id_range(item, is_id_invalid_improved)

print_pink(f'*** puzzle 2: {ans2} ***')
