from collections import deque


food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders and food_quantity >= orders[0]:
    food_quantity -= orders.popleft()

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")