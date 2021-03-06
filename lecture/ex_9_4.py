def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark/0.5)*0.5

marks = {}
max_points = input('Max Points: ')

while True:
    name = input('Name: ')
    if name == 'exit':
        break
    points = input('Points: ')
    marks[name] = calculate_mark(points, max_points)

for (name, mark) in marks.items(): #iteritems for python 2.7
    if mark >= 4:
        print(name + ' has passed with ' + str(mark))
    else:
        print(name + ' has failed with ' + str(mark))
print('Bye bye')