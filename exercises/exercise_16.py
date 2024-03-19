# Your solution to Exercise 16

steps = int(input())

for i in range(steps):
    print(" " * (steps - i - 1) + "#" * (i + 1))