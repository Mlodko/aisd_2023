from math import sqrt
from random import randint


def distance(a_coords, b_coords):
    return sqrt((a_coords[0] - b_coords[0]) ** 2 + (a_coords[1] - b_coords[1]) ** 2)

# Load
cities = []
with open('./TSP.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split()
        cities.append([float(split_line[1]), float(split_line[2])])

path = []
to_visit = [i for i in range(1,101)]
full_distance = 0.0
moves = 0

# Choose starting city
start = randint(1,100)
current = start

while moves <= 100:
    if moves == 100:
        destination = start
        min_distance = distance(cities[current - 1], cities[start - 1])
    else:
        distances = []
        min_distance = 100000000000000000
        for city in to_visit:
            checked = distance(cities[current - 1], cities[city - 1])
            distances.append((city, checked))
            if checked < min_distance:
                min_distance = checked
        for city in distances:
            if city[1] == min_distance:
                destination = city[0]
        to_visit.remove(destination)
    path.append(destination)
    current = destination
    moves += 1
    full_distance += min_distance

print(path)
print(len(path))
print(full_distance)


