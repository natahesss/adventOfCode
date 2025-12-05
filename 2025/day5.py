from helpers import print_pink

with open('inputs/day5.txt') as f:
    fresh_ranges, available = f.read().split('\n\n')


def compose_ranges(ranges: list) -> list:
    result = []
    ranges = [tuple(map(int, range.split('-'))) for range in ranges]
    ranges.sort(key=lambda x: x[0])

    for range in ranges:
        start, end = range
        for ind, item in enumerate(result):
            if item[0] <= start <= item[1]:
                result[ind] = (item[0], max(end, item[1]))
                break
        else:
            result.append((start, end))
    return result


def check_in_range(ranges: list, x: int) -> bool:
    for item in ranges:
        if x < item[0]:
            continue
        else:
            if item[0] <= x <= item[1]:
                return True
    return False


fresh_ranges = compose_ranges(fresh_ranges.split('\n'))
available = list(map(int, available.split('\n')))

ans1 = 0
for i in available:
    ans1 += int(check_in_range(fresh_ranges, i))

print_pink(f'*** puzzle 1: {ans1} ***')

ans2 = 0
for item in fresh_ranges:
    ans2 += item[1] - item[0] + 1

print_pink(f'*** puzzle 1: {ans2} ***')
