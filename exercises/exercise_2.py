n = input()
m = int(input())

output = ""
if m == 1:
    output = n

else:
    for _ in range(m):
        output += n + " "

print(output)