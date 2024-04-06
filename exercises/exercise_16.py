steps = int(input())

count = steps

if count > 6:
    count -= 1

string = ""
for i in range(1, steps + 1):
    count -= 1
    string = " " * count + "#" * i
    print(string)