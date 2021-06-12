import csv, json


def test_books():
    with open('books.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            yield {"title": line[0], "author": line[1], "height": line[3], "publisher": line[4]}


book = test_books()
next(book)
as_in_example = []

with open('users.json') as users:
    users_list = json.load(users)
    for user in users_list:
        user_4_add = {}
        user_4_add["name"] = user["name"]
        user_4_add["gender"] = user["gender"]
        user_4_add["address"] = user["address"]
        book_4_add = []
        book_4_add.append(next(book))
        user_4_add["book"] = book_4_add  #   Addng thirst book  to user
        book_4_add_2 = []
        book_4_add_2.append(next(book))
        user_4_add["book_2"] = book_4_add_2   # Adding second book to user     
        as_in_example.append(user_4_add)

with open('as_in_example.json', 'w') as file_2:  # Create the json file as in example
    json.dump(as_in_example, file_2, indent=4)

print('\n---Task is done---')