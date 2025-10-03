rows, cols = [int(x) for x in input().split()]

start_char = ord('a')

for r in range(rows):
    print()
    for c in range(cols):
        print(f"{chr(start_char + r)}{chr(start_char + c + r)}{chr(start_char + r)}", end=' ')