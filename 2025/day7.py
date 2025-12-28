from helpers import print_pink

with open('inputs/day7.txt') as f:
    lines = list(map(str.strip, f.readlines()))

start = lines[0].index('S')
width = len(lines[0])
beams = [0] * width
beams[start] = 1

ans1 = 0
ans2 = 0
for line in lines[1:]:
    for i in range(width):
        if line[i] == '^' and beams[i] > 0:
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            ans1 += 1
            beams[i] = 0

ans2 = sum(beams)

print_pink(f'*** puzzle 1: {ans1} ***')
print_pink(f'*** puzzle 2: {ans2} ***')
