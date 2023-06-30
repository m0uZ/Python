# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

path = "C:/Program/Python/task.py"


def getPathInfo_v1(path):
    arr_path = path.split("/")
    result_path = ""
    file = arr_path[-1].split(".")
    for i in range(len(arr_path) - 1):
        result_path += arr_path[i] + "/"

    return (result_path, file[0], file[1])


def getPathInfo_v2(path):

    file = path.split('/')[-1]
    file_name_split = file.split('.')
    file_extension = file_name_split[-1]
    file_name = '.'.join(file_name_split[:-1])
    path_without_filename = path[:-len(file)]

    return (path_without_filename, file_name, file_extension)
