# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def key_to_dict(**kwargs):
    res = {}
    for key, value in kwargs.items():
        if hasattr(value, '__hash__'): # Если ключ не является хешируемым типом, то преобразовываем его в строку.
            key_str = str(value)
        else:
            key_str = value
        res[key_str] = key
    return res


result = key_to_dict(a=1, b=2, c='hello', d=[1, 2, 3])
print(result)
