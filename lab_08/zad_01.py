import random
from math import sqrt
from copy import deepcopy


def distance(a_coords, b_coords):
    return sqrt((a_coords[0] - b_coords[0]) ** 2 + (a_coords[1] - b_coords[1]) ** 2)


# Load
cities = []
with open('./TSP.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split()
        cities.append([float(split_line[1]), float(split_line[2])])

path = []
to_visit = [i for i in range(1, 101)]
full_distance = 0.0
moves = 0
# Choose starting city
start = random.randint(1, 100)
print(start)
to_visit.remove(start)
path.append(start)
current = start
while moves <= 100:
    print(f"Move {moves}")
    if moves == 100:
        destination = start
    else:
        while True:
            destination = to_visit[random.randint(0,len(to_visit) - 1)]
            if moves == 99:
                print()
            if destination != start:
                to_visit.remove(destination)
                break
    current_coords = cities[current - 1]
    dest_coords = cities[destination - 1]
    #path.append((destination, distance(current_coords, dest_coords)))
    path.append(destination)
    current = destination
    full_distance += distance(current_coords, dest_coords)
    moves += 1

print(path)
print(len(path))
print(full_distance)
