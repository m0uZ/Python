# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:

# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона

from random import choices, randint
from string import ascii_letters, digits


def make_files(extension, min_name = 6, max_name = 30,
            min_size = 256, max_size = 4096, count = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters+digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)