import math

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = int(input('Input point for x1: '))
x2 = int(input('Input point for x2: '))
y1 = int(input('Input point for y1: '))
y2 = int(input('Input point for y2: '))

dist = int(distance(x1, x2, y1, y2))
print(dist)