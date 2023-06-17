# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

import random

number = random.randint(0, 1000)
tries = 10
guess = None

print("Угадайте число от 0 до 1000 за 10 попыток.")

while tries > 0:
    guess = int(input("Введите вашу догадку: "))
    
    if guess < number:
        print("Число больше вашей догадки.")
    elif guess > number:
        print("Число меньше вашей догадки.")
    else:
        print("Вы угадали число!")
        break
        
    tries -= 1
    print(f"У вас осталось {tries} попыток.")
    
if guess != number:
    print("Вы проиграли. Было загадано число", number)