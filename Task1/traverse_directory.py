import csv
import json
import os.path
import pickle


def get_size(path: str):
    if os.path.isfile(path):
        return os.path.getsize(path)

    elif os.path.isdir(path):
        total_size = 0

        for dir_path, _, file_names in os.walk(path):
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                total_size += os.path.getsize(file_path)

        return total_size


def traverse_directory(directory: str):
    result = list()

    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)


            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })

    return result


def save_to_json(data, file_name: str):
    with open(file_name, 'w', encoding='utf_8') as write_json:
        json.dump(data, write_json, indent=4, ensure_ascii=False)


def save_to_csv(data, filename: str):
    with open(filename, 'w', newline='') as write_csv:
        keys_names = ['name', 'path', 'type', 'size', 'parent']
        writer = csv.DictWriter(write_csv, fieldnames=keys_names)
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, file_name: str):
    with open(file_name, 'wb') as write_pickle:
        pickle.dump(data, write_pickle)


def main(directory):

    data = traverse_directory(directory)

    save_to_json(data=data, file_name='dir_info.json')
    save_to_csv(data=data, filename='dir_info.csv')
    save_to_pickle(data=data, file_name='dir_info.pickle')



if __name__ == '__main__':
    main("E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les8\Task2")