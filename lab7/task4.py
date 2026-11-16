r, c = map(int, input().split())
table = []
row_sums = []
col_sums = [0] * c

for i in range(r):
    row = list(map(int, input().split()))
    table.append(row)
    s = 0
    for j in range(c):
        s += row[j]
        col_sums[j] += row[j]
    row_sums.append(s)
  
print("Суммы строк:", row_sums)
print("Суммы столбцов:", col_sums)
