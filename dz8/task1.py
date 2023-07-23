# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
#     Для дочерних объектов указывайте родительскую директорию.
#     Для каждого объекта укажите файл это или директория.
#     Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import csv
import json
import os
import pickle
from pathlib import Path

PATH = Path(f'/home/ilya/Unity/Hub/Editor/2021.3.17f1/Editor/BugReporter/')


def scan_directory_and_write_info(main_path, file_name='tsk'):
    if not main_path.is_dir():
        raise Exception("Указанный каталог не доступен")
    lst_objs = []
    lst_paths = [main_path]
    while lst_paths:
        path = lst_paths.pop(0)
        for obj in os.listdir(path):
            dir_obj = {'object': obj, 'parent_dir': None, 'type_obj': None, 'size': None}
            if Path(Path(path) / obj).is_dir():
                lst_paths.append(Path(Path(path) / obj))
                dir_obj['type_obj'] = 'directory'
            if dir_obj['type_obj'] is None:
                dir_obj['type_obj'] = 'file'
            dir_obj['size'] = get_size_dir(Path(Path(path) / obj))
            dir_obj['parent_dir'] = str(path).replace(str(main_path), '')
            lst_objs.append(dir_obj)
    write_to_files(lst_objs, file_name=file_name)


def get_size_dir(path):
    if path.is_file():
        return os.path.getsize(path)
    size = 0
    for root, _, files in os.walk(path):
        for file in files:
            size += os.path.getsize(Path(Path(root) / file))
    return size


def write_to_files(lst_dict, file_name='tsk'):
    with (
        open(Path(Path().cwd() / f'{file_name}.bin'), 'wb') as file_pickle,
        open(Path(Path().cwd() / f'{file_name}.json'), 'w', encoding='UTF-8') as file_json,
        open(Path(Path().cwd() / f'{file_name}.csv'), 'w', encoding='UTF-8') as file_csv,
    ):
        json.dump(lst_dict, file_json, indent=2)
        pickle.dump(lst_dict, file_pickle)
        writer = csv.DictWriter(file_csv, fieldnames=lst_dict[0].keys(), dialect='excel-tab')
        writer.writeheader()
        writer.writerows(lst_dict)