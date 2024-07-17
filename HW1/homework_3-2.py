import random

def get_user_input():
    while True:
        try:
            min_number = int(input("Введіть мінімальний номер лотерейних квитків: "))
            max_number = int(input("Введіть максимальний номер лотерейних квитків: "))
            quantity = int(input("Введіть кількість виграшних лотерейних квитків: "))
            
            if min_number < 1:
                print("Мінімальний номер повинен бути більшим або рівним 1.")
                continue
            
            if max_number > 1000:
                print("Максимальний номер повинен бути меншим або рівним 1000.")
                continue
            
            if quantity > (max_number - min_number + 1):
                print("Кількість виграшних квитків перевищує діапазон доступних квитків.")
                continue

            return min_number, max_number, quantity
        
        except ValueError:
            print("Введіть ціле число.")

def get_numbers_ticket(min_number, max_number, quantity):
    list_ticket = list(range(min_number, max_number + 1))  # Створення списку номерів квитків
    victory_tickets = random.sample(list_ticket, quantity)  # Випадковий вибір виграшних квитків
    victory_tickets.sort()  # Сортування виграшних квитків
    return victory_tickets

# Отримання введення від користувача
min_number, max_number, quantity = get_user_input()

# Отримання виграшних номерів квитків
ticket_numbers = get_numbers_ticket(min_number, max_number, quantity)

# Виведення виграшних номерів
print("Виграшні номери квитків:", ticket_numbers)
