add_term = 1
total = 0
count = 0

while add_term == 1:
    term = int(input())
    if term == 0:
        break
    total += term
    count += 1

print(total / count)