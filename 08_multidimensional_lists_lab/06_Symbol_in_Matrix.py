rows = int(input())
matrix = []

for _ in range(rows):
    row = [x for x in input()]
    matrix.append(row)

search = input()
found = False

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == search:
            print(f"({r}, {c})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{search} does not occur in the matrix")