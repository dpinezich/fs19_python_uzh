import json

address_book_file = open('address_book.txt', 'r')
address_book_dict = json.load(address_book_file)

while True:
    requested_name = input('Name of the person: ')
    if requested_name == 'exit':
        break
    else:
        if requested_name in address_book_dict:
            print(address_book_dict[requested_name])
        else:
            print('Person not found')


address_book_file.close()