import math
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]


coordinates = []

with open(file1) as f1, open(file2) as f2:
    x_coordinate, y_coordinate = map(float, next(f1).rstrip().split(' '))
    radius = float(next(f1).rstrip())

    for line in f2:
        coordinates.append(tuple(map(float, line.rstrip().split(' '))))

for tup in coordinates:
    x = tup[0] - x_coordinate
    y = tup[1] - y_coordinate
    if math.sqrt(x**2 + y**2) < radius:
        print(1)
    elif math.sqrt(x**2 + y**2) == radius:
        print(0)
    else:
        print(2)
