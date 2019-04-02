
import math

def volume_from_points(x1, x2, y1, y2):
    return volume(distance(x1, x2, y1, y2))

def volume(radius):
    return 4.0/3.0 * math.pi * radius**3

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = int(input('Input point for x1: '))
x2 = int(input('Input point for x2: '))
y1 = int(input('Input point for y1: '))
y2 = int(input('Input point for y2: '))

print(volume_from_points(x1, x2, y1, y2))