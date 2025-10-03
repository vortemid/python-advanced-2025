first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

for _ in range(int(input())):
    line = input().split()
    command = line[0] + ' ' + line[1]
    numbers = [int(x) for x in line[2:]]
    
    if command == "Add First":
        first_seq.update(numbers)
    elif command == "Add Second":
        second_seq.update(numbers)
    elif command == "Remove First":
        first_seq.difference_update(numbers)
    elif command == "Remove Second":
        second_seq.difference_update(numbers)
    elif command == "Check Subset":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')