train_data = input()

parts = train_data.split(';')

train_number = parts[0]
from_city = parts[1]
to_city = parts[2]
time = parts[3]
price = float(parts[4])

price_formatted = "%.2f" % price

print("Поезд: " + train_number)
print("Маршрут: " + from_city + " - " + to_city)
print("Отправление: " + time)
print("Цена: " + price_formatted + " руб")