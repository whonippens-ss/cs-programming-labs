n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        row = ""
        for j in range(n):
            if i > j:
                d = i - j
            else:
                d = j - i
            if j > 0:
                row += " "
            row += str(d)
        print(row)
