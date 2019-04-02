

def print_reverse_for(text):
    str = ''
    for char in text:
        str = char + str
    print(str)

string = input('String: ')
print_reverse_for(string)
