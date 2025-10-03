longest_intersection = set()

for _ in range(int(input())):
    # str = input().split("-")
    # first = set(range(int(str[0].split(',')[0]), int(str[0].split(',')[1]) + 1, 1))
    # second = set(range(int(str[1].split(',')[0]), int(str[1].split(',')[1]) + 1, 1))

    first, second = (set(range(int(x.split(',')[0]), int(x.split(',')[1]) + 1, 1)) for x in input().split("-"))

    if len(first & second) > len(longest_intersection):
        longest_intersection = first & second

print(f"Longest intersection is {sorted(list(longest_intersection))} with length {len(longest_intersection )}")