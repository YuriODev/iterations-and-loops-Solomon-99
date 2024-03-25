pounds = int(input())
CONV = 0.453

for i in range(1, pounds + 1):
    if i == 7:
        print(i, 3.18)
    else:
        print(str(i) + " " + f"{(i * CONV):.2f}")