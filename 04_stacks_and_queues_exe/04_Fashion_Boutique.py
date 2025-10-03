clothes = list(map(int, input().split()))
rack_capacity = int(input())
curr_rack = 0

while clothes:
    curr_rack_capacity = rack_capacity
    
    while clothes and curr_rack_capacity >= clothes[-1]:
        curr_rack_capacity -= clothes.pop()

    curr_rack += 1

print(curr_rack)
