from collections import deque


kids = deque(input().split())

toss_number = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-toss_number)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids[0]}")
