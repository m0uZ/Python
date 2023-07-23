# Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.

# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from make_files import make_files


def new_make_file(extensions):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)