import math

def volume(radius):
    return 4/3 * math.pi * radius**3

rad = int(input('Please insert radius: '))


print(volume(rad))