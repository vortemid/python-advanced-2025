odd_set = set()
even_set = set()

for index in range(1, int(input()) + 1):
    name = input()
    sum_ascii = 0
    for ch in name:
        sum_ascii += ord(ch)

    devide = sum_ascii // index

    if devide % 2 == 0:
        even_set.add(devide)
    else:
        odd_set.add(devide)

if sum(odd_set) == sum(even_set):
    print(", ".join([str(x) for x in odd_set.union(even_set)]))
elif sum(odd_set) > sum(even_set):
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
elif sum(even_set) > sum(odd_set):
    print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))