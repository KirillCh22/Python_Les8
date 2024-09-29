import csv
import json


def main():

    dict_books = dict()

    with open('books.scv', 'r', newline='') as csv_read:
        reader = csv.DictReader(csv_read)

        for row in reader:
            author = row['author']
            book = {
                'name_book': row['name_book']
            }

        if author in dict_books:
            dict_books[author] += book
        else:
            dict_books[author] = book


    with open('books_by_author.json', 'w') as write_json:
        json.dump(dict_books, write_json, indent=4)

if __name__ == '__main__':
    main()