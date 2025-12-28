from math import sqrt, prod

from helpers import print_pink

with open('inputs/day8.txt') as f:
    lines = list(map(lambda line: tuple(map(int, line.strip().split(','))), f.readlines()))


def get_distance(coords1: tuple, coords3: tuple) -> float:
    return sqrt((coords1[0] - coords3[0]) ** 2 + (coords1[1] - coords3[1]) ** 2 + (coords1[2] - coords3[2]) ** 2)


connections = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        dist = get_distance(lines[i], lines[j])
        connections.append((get_distance(lines[i], lines[j]), lines[i], lines[j]))

connections.sort(key=lambda x: x[0])

circuits = [{line} for line in lines]

n = 1000
for connection in connections:
    found_circuits = []
    coords = connection[1:]
    for i, circuit in enumerate(circuits):
        if coords[0] in circuit or coords[1] in circuit:
            found_circuits.append(i)

    if len(found_circuits) == 0:
        circuits.append(set(coords))
    else:
        circuits[found_circuits[0]].update(coords)
        if len(found_circuits) == 2:
            circuits[found_circuits[0]].update(circuits[found_circuits[1]])
            del circuits[found_circuits[1]]

    n -= 1
    if n == 0:
        circuits_lengths = [len(circuit) for circuit in circuits]
        circuits_lengths.sort(reverse=True)
        ans1 = prod(circuits_lengths[:3])

    if len(circuits) == 1:
        ans2 = coords[0][0] * coords[1][0]
        break

print_pink(f'*** puzzle 1: {ans1} ***')
print_pink(f'*** puzzle 1: {ans2} ***')
