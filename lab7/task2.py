numbers = list(map(int, input().split()))
squares = [x ** 2 for x in numbers if x > 0 and x % 2 == 1]
print("Квадраты:", squares)
