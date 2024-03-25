num_Of_Ints = int(input())
num_Of_Zeros = 0

for i in range(num_Of_Ints):
    num = input()
    for char in num:
        num_Of_Zeros += 1 if char == "0" else 0

print(num_Of_Zeros)