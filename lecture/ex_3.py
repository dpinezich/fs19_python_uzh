def compare(x, y):
    if x > y:
        print(1)
    elif x == y:
        print(0)
    else:
        print(-1)

x = int(input('Fist number: '))
y = int(input('Second number: '))

compare(x, y)