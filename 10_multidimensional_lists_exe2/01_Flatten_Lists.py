txt = input().split('|')

matrix = []

for i in range(len(txt)):
    row = txt[i].split()
    if row:
        matrix.append(row)

[print(*row, sep=" ", end=" ") for row in reversed(matrix)]