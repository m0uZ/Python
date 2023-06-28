# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются,
# а помещаются в одноимённые переменные без s на конце.

eggs = 5
tomatoes = 10
potatoes = 3
sugar = 2
s = 34

def replace_s_vars():
    for var_name in list(globals()):
        if var_name != "s" and var_name.endswith("s"):
            globals()[var_name[:-1]] = globals()[var_name]
            del globals()[var_name]
            globals()[var_name] = None


replace_s_vars()
print(eggs, egg) # переменная egg создалась через globals  хотя и не обьявляясь в коде
