rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

prim_diagonal = [matrix[i][i] for i in range(rows)]
sec_diagonal = [matrix[i][rows - 1 - i] for i in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in prim_diagonal)}. Sum: {sum(prim_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in sec_diagonal)}. Sum: {sum(sec_diagonal)}")