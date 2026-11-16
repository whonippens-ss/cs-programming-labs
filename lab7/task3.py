numbers = list(map(int, input().split()))
target = int(input())
indexi = []

for index, number in enumerate(numbers):
    if number == target:
        indexi.append(index)
      
print(f'Индексы: {indexi}')
