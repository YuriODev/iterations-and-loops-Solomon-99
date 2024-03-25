n = int(input())
m = int(input())
for i in range(n+1):
    if n == 3 and i == 3:
        break
    string = '\t' + str(i)
    string = string * (m - 2)
    string = str(i) + '\t' + str(i) + string
    if m == 7:
        string = string + '\t' + str(i)
    print(string)