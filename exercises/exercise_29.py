numbers = []
total = 0
squares = 0

while True:
    number = int(input())
    numbers.append(number)
    total += number
    squares += number ** 2
    if total == 0:
        break

print(squares//2)