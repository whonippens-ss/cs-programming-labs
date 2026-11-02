n = int(input())
count = 0
for r in range(n):
    c = 1
    for k in range(r + 1):
        print(c, end=" ")
        if c % 2 == 1:
            count += 1
        c = c * (r - k) // (k + 1)
    print()
print("Нечетных элементов:", count)
