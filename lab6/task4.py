n = int(input())

if n < 0:
    print('Ошибка')
else:
    c = 0
    s = 0
    
    if n == 0:
        c = 1
        s = 0
    else:
        while n > 0:
            d = n % 10
            s += d
            c += 1
            n = n // 10
            
    print(f'Цифр: {c}')
    print(f'Сумма цифр: {s}')
