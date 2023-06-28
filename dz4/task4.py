# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# Напишите программу банкомат. Начальная сумма равна нулю 
# Допустимые действия: пополнить, снять, выйти Сумма пополнения и снятия кратны 50 у.е. 
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. 
# После каждой третей операции пополнения или снятия начисляются проценты - 3% 
# Нельзя снять больше, чем на счёте При превышении суммы в 5 млн, 
# вычитать налог на богатство 10% перед каждой операцией, даже ошибочной 
# Любое действие выводит сумму денег.

def deposit(balance):
    amount = int(input("Введите сумму для пополнения: "))
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50!")
    else:
        balance += amount
        print("Счет пополнен на: ", amount, "у.е.")
        print("Текущая сумма на счете:", balance, "у.е.")
    return balance


def withdraw(balance):
    amount = int(input("Введите сумму для снятия: "))

    if amount > balance:
        print("Недостаточно средств на счете!")
    elif amount % 50 != 0:
        print("Сумма должна быть кратна 50!")
    else:
        commission = amount * 0.015
        commission = max(commission, 30)
        commission = min(commission, 600)
        balance -= amount + commission
        print("Снято: ", amount, "у.е.")
        print("Комиссия составила: ", commission, "у.е.")
        print("Текущая сумма на счете: ", balance, "у.е.")

    return balance


def show_balance(balance):
    print("Текущая сумма на счете:", balance, "у.е.")


def main():
    count = 0
    balance = 0

    while True:
        if balance >= 5000000:
            tax = balance * 0.1
            balance -= tax
            print("Применен налог на богатство в размере", tax, "у.е.")
            print("Текущая сумма на счете:", balance, "у.е.")

        action = input("Выберите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            balance = deposit(balance)
            count += 1
        elif action == "снять":
            balance = withdraw(balance)
            count += 1
        elif action == "выйти":
            break
        else:
            print("Некорректное действие!")

        if count % 3 == 0:
            interest = balance * 0.03
            balance += interest
            print("Начислены проценты на сумму", interest, "у.е.")
            print("Текущая сумма на счете:", balance, "у.е.")

        show_balance(balance)

    print("Спасибо за использование наших услуг!")


main()
