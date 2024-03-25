number = int(input())
total = 0

for i in range(100, 1000):
    hundreds = i // 100
    tens = (i // 10) % 10
    ones = i % 10

    if hundreds + tens + ones == number:
        total += 1

print(total)