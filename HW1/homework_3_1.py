from datetime import datetime

def get_date_input():
    while True:
        try:
            date_string = input("Будь ласка, введіть дату у форматі день-місяць-рік (наприклад, 26-06-2024): ")
            datetime_object = datetime.strptime(date_string, "%d-%m-%Y")
            return datetime_object
        except ValueError:
            print("Дата введена неправильно, спробуйте ще раз")

def get_days_from_today(date) -> int:
    today = datetime.today()
    difference = date.toordinal() - today.toordinal()
    return difference

# Отримання дати від користувача
date = get_date_input()

# Обчислення різниці в днях
difference_result = get_days_from_today(date)

# Виведення результату
print(f"Різниця між датами: {difference_result} днів")