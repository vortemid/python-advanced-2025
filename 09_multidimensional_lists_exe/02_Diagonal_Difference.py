rows = int(input())

matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]

prim_diagonal = [matrix[i][i] for i in range(rows)]
sec_diagonal = [matrix[i][rows - 1 - i] for i in range(rows)]

print(abs(sum(prim_diagonal) - sum(sec_diagonal)))