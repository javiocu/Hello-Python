### Strings ###

from datetime import datetime # Es un módulo que contienen todo lo necesario para trabajar con fechas


now = datetime.now()

timestamp = now.timestamp()

print(timestamp)


year_2023 = datetime(2023, 1, 1)

def print_date (date):
    print(date.year)
    print(date.day)
    print(date.month)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(year_2023)

print("---------------------------------------------------")

from datetime import time  # Time también del módulo datetime, nos permite introducir fechas que queramos, en el caso de datetime trabajamos con las fechas que hay ya


current_time = time(13, 23, 0)  # Para representar horas solo

print(current_time.hour)

print("---------------------------------------------------")

from datetime import date

current_date = date(2023, 10, 3)

print(current_date.year) # Date sirve para representar solamente fechas sin horas, de nuevo las que introduzcamos nosotros, para representar
print(current_date.month)
print(current_date.day)

print(current_date - date(2022, 12, 1))


from datetime import timedelta


time_delta = timedelta(12, 23,)
