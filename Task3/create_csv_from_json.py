import csv
import json


def main():



    with open('E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les8\Task3\products.json', 'r', encoding='utf-8') as file_load:
        list_json = (json.load(file_load))


    with open('products.csv', 'w', newline='') as csv_write:
        writer = csv.DictWriter(csv_write, fieldnames=list(list_json[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for string_file in list_json:
            writer.writerow(string_file)


if __name__ == '__main__':
    main()
