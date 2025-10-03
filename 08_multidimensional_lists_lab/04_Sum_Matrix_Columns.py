rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)