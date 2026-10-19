base_price = float(input())
age = int(input())

if base_price <= 0 or not (0 <= age <= 120):
 print("Ошибка")
elif age <= 5:
 print(f"Стоимость: {base_price * 0.00:.2f} руб")
elif age <= 17:
 print(f"Стоимость: {base_price * 0.50:.2f} руб")
elif age <= 59:
 print(f"Стоимость: {base_price * 1.00:.2f} руб")
else:
 print(f"Стоимость: {base_price * 0.70:.2f} руб")