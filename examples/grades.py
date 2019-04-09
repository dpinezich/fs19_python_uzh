

def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return mark

max_points = 20
marks = {}


while True:
    points = input('Points: ')
    if points == 'exit':
        print('Bye Bye')
        break
    name = input('Name: ')
    marks[name] = calculate_mark(int(points), max_points)


for (name, mark) in marks.items():
    if mark >= 4:
        print("Hello " + name + " you passed with a mark of: " + str(mark))
    else:
        print("Hello " + name + " you failed with a mark of: " + str(mark))