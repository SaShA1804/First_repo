import random

min = 1
max = int(input("Ведіть максимальний  номер в лотерейних квитків : "))
quantity = int(input("Ведіть кількість вийграшних лотерейних квитків:"))

def get_number_ticket(min,max,quantity):
    list_ticket=[]

    for number in range(min,max+1):
        list_ticket.append(number)

    victory_tickets=random.sample(list_ticket,quantity)
    victory_tickets_sort = sorted(victory_tickets)
    return victory_tickets_sort

ticket_number=get_number_ticket(min,max,quantity)
print(ticket_number)