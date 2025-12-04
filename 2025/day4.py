from helpers import print_pink

with open('inputs/day4.txt') as f:
    start_matrix = [list(line.strip()) for line in f.readlines()]


def find_accessible_paper(mx: list) -> list:
    coords = []
    height = len(mx)
    width = len(mx[0])

    for i in range(height):
        for j in range(width):
            if mx[i][j] != '@':
                continue

            obstacles = 0
            for k in range(i - 1, i + 2):
                # out of matrix
                if k < 0 or k >= height:
                    continue
                # too many obstacles - check failed
                if obstacles >= 4:
                    break

                for l in range(j - 1, j + 2):
                    # out of matrix
                    if l < 0 or l >= width:
                        continue
                    # exclude coordinates of target roll
                    if k == i and l == j:
                        continue
                    # obstacle found
                    if mx[k][l] == '@':
                        obstacles += 1
                    # too many obstacles - check failed
                    if obstacles >= 4:
                        break

            if obstacles < 4:
                coords.append([i, j])

    return coords


first_coords = find_accessible_paper(start_matrix)
ans1 = len(first_coords)

print_pink(f'*** puzzle 1: {ans1} ***')

ans2 = ans1
for coord in first_coords:
    start_matrix[coord[0]][coord[1]] = '.'
while True:
    new_coords = find_accessible_paper(start_matrix)
    if not new_coords:
        break
    ans2 += len(new_coords)
    for coord in new_coords:
        start_matrix[coord[0]][coord[1]] = '.'

print_pink(f'*** puzzle 2: {ans2} ***')
