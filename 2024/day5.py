from functools import reduce

from helpers import print_blue, print_pink

with open('inputs/day5.txt') as inf:
    rules, updates = map(lambda x: x.split('\n'), inf.read().split('\n\n'))

updates = list(map(lambda x: x.split(','), updates))

def create_rule_dict(rules: list) -> dict:
    rule_dict = {}
    for r in rules:
        left, right = r.split('|')
        rule_dict.setdefault(left, []).append(right)
        rule_dict.setdefault(right, [])

    return rule_dict

def check_update_v2(update: list, rule_dict: dict) -> bool:
    for i in range(len(update) - 1):
        if update[i + 1] not in rule_dict[update[i]]:
            return False
    return True

def get_sum_of_middle_values(lst: list) -> int:
    middles = list(map(lambda x: x[(len(x) - 1) // 2], lst))
    return sum(map(int, middles))

rule_dict = create_rule_dict(rules)
filtered_updates = list(filter(lambda x: check_update_v2(x, rule_dict), updates))
ans = get_sum_of_middle_values(filtered_updates)

print_pink(f"*** puzzle 1: {ans} ***")

incorrect_updates = list(filter(lambda x: not check_update_v2(x, rule_dict), updates))
# print(incorrect_updates)

def reorder_update(update: list, rule: dict):
    good_job = False
    while not good_job:
        for i in range(len(update) - 1):
            if update[i + 1] not in rule[update[i]]:
                update[i], update[i + 1] = update[i + 1], update[i]
        if check_update_v2(update, rule):
            good_job = True
    return update

reordered_updates = list(map(lambda x: reorder_update(x, rule_dict), incorrect_updates))
ans2 = get_sum_of_middle_values(reordered_updates)

print_pink(f"*** puzzle 2: {ans2} ***")