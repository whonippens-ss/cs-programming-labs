numbers = list(map(int, input().split()))
fixed = numbers.copy()

for i in range(len(fixed)):
    if fixed[i] < 0:
        fixed[i] = 0
        
print("Исходные остатки:", numbers)
print("Исправленные остатки:", fixed)
