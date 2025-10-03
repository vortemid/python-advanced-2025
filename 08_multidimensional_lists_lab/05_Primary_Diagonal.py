rows = int(input())
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

diagonal_sum = 0
cross_diag_sum = 0

for i in range(rows):
    diagonal_sum += matrix[i][i]
    cross_diag_sum += matrix[i][rows - 1 - i]

print(diagonal_sum)
#print(cross_diag_sum)
