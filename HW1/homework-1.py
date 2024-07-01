from datetime import datetime 

def get_days_from_today():
    while True:
        try:
            date_string = input("Будь ласка, введіть дату у форматі день-місяць-рік (наприклад, 26-06-2024): ")
            datetime_object = datetime.strptime(date_string, "%d-%m-%Y")
            return datetime_object
        except ValueError:
            print("Дата ведена не правильно спробуй ще раз")
def get_days_difference(input_day)->int:
    today = datetime.today()
    difference =input_day.toordinal()-today.toordinal()
    return difference
input_date = get_days_from_today()
days_difference = get_days_difference(input_date)
print(f"різниця між датами {days_difference} днів")

