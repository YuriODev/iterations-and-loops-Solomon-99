upper_bound = int(input())

for i in range(1, upper_bound + 1):
    print(f"{i}" * (i % 2 == 1), end=" ")