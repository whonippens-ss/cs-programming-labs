a = int(input())
b = int(input())

c = 0  # сумма чисел
d = 1  # произведение чисел

for i in range(a, b + 1):  # i — счетчик
    c += i
    d *= i

print(f"Сумма: {c}")
print(f"Произведение: {d}")
