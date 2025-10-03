number_lines = int(input())
numbers = []

for _ in range(number_lines):
    line = input().split()
    if line[0] == '1':
        numbers.append(int(line[1]))
    elif numbers:
        if line[0] == '2':
            numbers.pop()
        elif line[0] == '3':
            print(max(numbers))
        elif line[0] == '4':
            print(min(numbers))

# while len(numbers) > 1:
#     print(numbers.pop(), end=", ")
# print(numbers.pop())

#print(', '.join(str(x) for x in reversed(numbers)))
print(*reversed(numbers), sep=', ')