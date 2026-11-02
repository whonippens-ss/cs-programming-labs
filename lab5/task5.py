count = 0
cost = 0

while True:
    try: n = int(input())
    except: break
    count += 1
    cost += n

print(f'Покупок: {count}')
print(f'Общая стоимость: {cost}')
print(f'Средняя стоимость: {cost / count}')
