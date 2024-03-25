n = int(input())
output = ""

for i in range(20, n + 1):
    output += str(i)
    if n == i:
        break
    output += " "

print(output)