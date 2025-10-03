rows, cols = [int(x) for x in input().split(', ')]
matrix = []
total = 0

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    total += sum(row)

print(total)
print(matrix)
