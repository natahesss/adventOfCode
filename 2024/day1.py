import csv

with open('inputs/day1.csv') as inf:
    data = map(lambda x: list(map(int, x[0].split('   '))),
               csv.reader(inf))
    columns = zip(*data)

columns = list(map(sorted, columns))
s = 0
for i in range(len(columns[0])):
    s += abs(columns[0][i] - columns[1][i])

print(f'*** puzzle 1: {s} ***')

sim_score = 0
for n in columns[0]:
    sim_score += columns[1].count(n) * n
print(f'*** puzzle 2: {sim_score} ***')