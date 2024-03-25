upper_bound = int(input())
total = 0

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

for i in range(1, upper_bound + 1):
    print(factorial(i))
    total += factorial(i)

print(total)