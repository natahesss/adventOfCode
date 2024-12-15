import csv

with open('inputs/day2.csv') as inf:
    data = list(map(lambda x: list(map(int, x)), csv.reader(inf, delimiter=' ')))

def check_direction(nums: list):
    if nums == sorted(nums):
        return True
    if nums == sorted(nums, reverse=True):
        return True
    return False

def check_difference(nums: list):
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) not in range(1, 4):
            return False
    return True

ans = len(list(filter(check_difference, (filter(check_direction, data)))))
print(f'*** puzzle 1: {ans} ***')

def tolerator(nums: list):
    if check_direction(nums) and check_difference(nums):
        return True
    for i in range(len(nums)):
        local_nums = nums.copy()
        local_nums.pop(i)
        if check_direction(local_nums) and check_difference(local_nums):
            return True
    return False

ans2 = len(list(filter(tolerator, data)))
print(f'*** puzzle 2: {ans2} ***')