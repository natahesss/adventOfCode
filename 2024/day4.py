from audioop import reverse

with open('inputs/day4.txt') as inf:
    data = [l.strip() for l in inf.readlines()]

width = len(data[0])
height = len(data)

counter = 0
for i in range(height):
    line_findings = []
    for j in range(width):
        if data[i][j] == 'X':
            # right
            if j + 3 < width:
                line_findings.append(data[i][j:j+4])
            # left
            if j - 3 >= 0:
                left = data[i][j-3:j+1][::-1]
                line_findings.append(left)
            # down
            if i <= height - 4:
                down = ''.join([data[i + x][j] for x in range(4)])
                line_findings.append(down)
            # up
            if i >= 3:
                up = ''.join([data[i - x][j] for x in range(4)])
                line_findings.append(up)
            # diagonal up right
            if i >= 3 and j + 3 < width:
                diag_up_right = ''.join([data[i - x][j + x] for x in range(4)])
                line_findings.append(diag_up_right)
            # diagonal down right
            if i <= height - 4 and j + 3 < width:
                diag_down_right = ''.join([data[i + x][j + x] for x in range(4)])
                line_findings.append(diag_down_right)
            # diagonal up left
            if i >= 3 and j - 3 >= 0:
                diag_up_left = ''.join([data[i - x][j - x] for x in range(4)])
                line_findings.append(diag_up_left)
            # diagonal down left
            if i <= height - 4 and j - 3 >= 0:
                diag_down_left = ''.join([data[i + x][j - x] for x in range(4)])
                line_findings.append(diag_down_left)

    counter += len(list(filter(lambda x: x == 'XMAS', line_findings)))

print(f'*** puzzle 1: {counter} ***')

counter2 = 0
for i in range(1, height-1):
    line_findings = []
    for j in range(1, width-1):
        if data[i][j] == 'A':
            diag_down_left = [data[i - 1][j - 1], data[i + 1][j + 1]]
            diag_down_right = [data[i - 1][j + 1], data[i + 1][j - 1]]
            if all(map(lambda x: x.count('M') == 1 and x.count('S') == 1,
                       [diag_down_left, diag_down_right])):
                counter2 += 1

print(f'*** puzzle 2: {counter2} ***')
