numbers = set(map(int, input().split()))
target_num = int(input())

for num in list(numbers):
    difference = target_num - num
    pair = set([num, difference])

    if pair <= numbers and len(pair) == 2:
        numbers = numbers - pair
        print(f"{num} + {difference} = {target_num}")
