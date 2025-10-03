num = tuple(float(x) for x in input().split())
numbers = {}

for el in num:
    if el not in numbers:
        numbers[el] = num.count(el)

for k,v in numbers.items():
    print(f"{k:.1f} - {v} times")
