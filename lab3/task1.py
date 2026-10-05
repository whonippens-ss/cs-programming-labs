code = input()

category = code[0:3]
year = code[4:8]
number = code[9:13]

reverse_number = number[::-1]

print("Категория: " + category)
print("Год: " + year)
print("Номер: " + number)
print("Обратный номер: " + reverse_number)
