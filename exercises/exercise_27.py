n = int(input())
operator = 1
pi = 0

for i in range(1,n * 2,2):
    if operator == 1:
        pi += (4 / i)
        operator = 0
    else:
        pi -= (4 / i)
        operator = 1

print(pi)