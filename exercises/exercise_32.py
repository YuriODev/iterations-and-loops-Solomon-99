speeds = []
num_Of_Cars = int(input())

for i in range(num_Of_Cars):
    speed = int(input())
    speeds.append(speed)

range_Of_Speeds = 0
less_Than_30 = 0

range_Of_Speeds = max(speeds) - min(speeds)

for speed in speeds:
    if speed <= 30:
        less_Than_30 += 1

print(range_Of_Speeds)
print(less_Than_30)