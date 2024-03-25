hours = int(input())
hours = hours // 2
cells = 1

for i in range(0, hours-1):
    cells += 2 ** i

print(cells)