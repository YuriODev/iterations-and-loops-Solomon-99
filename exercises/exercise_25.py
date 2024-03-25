distance = int(input())
target_distance = int(input())

days = 1
while distance < target_distance:
    distance *= 1.1
    days += 1

print(f"{distance:.2f} km, {days} days")