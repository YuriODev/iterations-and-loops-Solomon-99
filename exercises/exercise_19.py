number = int(input())

for i in range(10, 100):
    tens = i // 10
    ones = i % 10

    if ((tens ** 2) + (ones ** 2)) % number == 0:
        print(f"{i},", end="")