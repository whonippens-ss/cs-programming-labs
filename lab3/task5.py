identifier = input()

length = len(identifier)
only_letters = identifier.isalpha()
only_digits = identifier.isdigit()
alphanumeric = identifier.isalnum()
has_defis = '-' in identifier

print("Длина: " + str(length))
print("Только буквы: " + str(only_letters))
print("Только цифры: " + str(only_digits))
print("Буквенно-цифровая: " + str(alphanumeric))
print("Содержит дефис: " + str(has_defis))