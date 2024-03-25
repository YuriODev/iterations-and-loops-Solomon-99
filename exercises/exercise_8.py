n = int(input())
output = ""

for i in range(2, n + 1, 2):
    output += str(i)
    if i == n or n - 1 == i:
        break
    output += " "

print(output)