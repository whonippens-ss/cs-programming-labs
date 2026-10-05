fio = input()

parts = fio.split()

surname = parts[0].capitalize()
first_name_initial = parts[1][0].upper()
patronymic_initial = parts[2][0].upper()

print(surname + " " + first_name_initial + ". " + patronymic_initial + ".")