from collections import deque
from datetime import datetime, timedelta

robots = ({name: [int(time), datetime.strptime("00:00:00", "%H:%M:%S")] for name, time in (r.split("-") for r in input().split(";"))})
time_str = input()
start_time = datetime.strptime(time_str, "%H:%M:%S")
lowest_time = start_time
product = input()

products = deque()

while product != "End":
    products.append(product)
    product = input()

# print(start_time)
# print(robots)
# print(*products)

while products:
    curr_product = products.popleft()
    assigned = False
    start_time = start_time + timedelta(seconds=1)
    for name,time in robots.items():
        # print(time)
        if time[1] <= start_time:
            print(f"{name} - {curr_product} [{start_time.strftime('%H:%M:%S')}]")
            time[1] = start_time + timedelta(seconds=time[0])
            assigned = True
            break

    if assigned == False:
        products.append(curr_product)
