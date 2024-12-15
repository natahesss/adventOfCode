from itertools import combinations_with_replacement, product, permutations, combinations

from helpers import print_pink

with open('inputs/day7.txt', 'r') as f:
    data = list(f.readlines())

def can_be_evaluated(ans: int, row: list, operators: list):
    # all possible orders of math operators
    options = list(product(operators, repeat=len(row) - 1))

    # checking each combination
    for opt in options:
        res = row[0]
        # applying operators one by one
        for i in range(len(opt)):
            if opt[i] == '+':
                res += row[i + 1]
            elif opt[i] == '*':
                res *= row[i + 1]
            else:
                res = int(str(res) + str(row[i+1]))

            if res > ans:
                # break if the current result already exceeds the target
                break
        if res == ans:
            return True
    return False

sum = 0
sum2 = 0
for line in data:
    ans, row = line.split(': ')
    ans = int(ans)
    row = list(map(int, row.split(' ')))
    if can_be_evaluated(ans, row, ['+', '*']):
        sum += ans
        sum2 += ans
    else:
        if can_be_evaluated(ans, row, ['+', '*', '||']):
            sum2 += ans

print_pink(f"*** puzzle 1: {sum} ***")
print_pink(f"*** puzzle 2: {sum2} ***")


