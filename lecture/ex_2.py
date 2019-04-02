import math

def volume_from_radius(radius):
    return 4.0/3.0 * math.pi * radius**3

radius = int(input('Radius: '))

print(volume_from_radius(radius))