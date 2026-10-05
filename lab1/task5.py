distance = float(input())
consumption = float(input())
price = float(input())

fuel_quantity = (distance / 100) * consumption
cost = fuel_quantity * price

print("Топливо: %.2f л" % fuel_quantity)
print("Стоимость: %.2f руб" % cost)