n = int(input())
below = equal = above = 0

for _ in range(n):
    temp = float(input())
    if temp < 0: below += 1
    elif temp == 0: equal += 1
    else: above += 1

print(f"Ниже нуля: {below}")
print(f"Равны нулю: {equal}")
print(f"Выше нуля: {above}")
