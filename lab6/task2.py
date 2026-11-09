n = int(input())
if n < 2:
    print("Не простое")
else:
    for g in range(2, int(n**0.5) + 1):
        if n % g == 0:
            print("Не простое")
            break
    else:
        print("Простое")
