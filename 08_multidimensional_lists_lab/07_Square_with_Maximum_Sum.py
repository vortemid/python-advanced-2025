rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

sum_submatrix = 0

for r in range(rows - 1):
    for c in range (cols - 1):
        curr_submatrix = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if curr_submatrix > sum_submatrix:
            sum_submatrix = curr_submatrix
            curr_el = matrix[r][c]
            next_el = matrix[r][c + 1]
            under_el = matrix[r + 1][c]
            diag_el = matrix[r + 1][c + 1]
            
print(curr_el, next_el)
print(under_el, diag_el)
print(sum_submatrix)
