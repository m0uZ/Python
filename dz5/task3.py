# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()
for _ in range(10):
    x = next(gen)
    print(x)
