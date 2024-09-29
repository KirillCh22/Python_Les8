import glob
import json
import csv

def main():

    arr_path = list()
    for list_file in glob.glob("E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les8\Task2\*"):
        arr_path.append(list_file)

    concate_file = list()

    with (
        open(arr_path[1], 'r', encoding='utf-8') as file_1,
        open(arr_path[2], 'r', encoding='utf-8') as file_2,
        open(arr_path[3], 'r', encoding='utf-8') as file_3
    ):
        date_file_1 = json.load(file_1)
        date_file_2 = json.load(file_2)
        date_file_3 = json.load(file_3)

    concate_file.extend(date_file_1)
    concate_file.extend(date_file_2)
    concate_file.extend(date_file_3)

    print(concate_file)

    with open('concate_json.json', 'w') as file_write:
        json.dump(concate_file, file_write)


if __name__ == '__main__':
    main()