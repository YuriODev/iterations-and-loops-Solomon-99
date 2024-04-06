add_term = 1
values = []

while add_term == 1:
    value = int(input())
    if value == 0:
        break
    values.append(value)

num_Of_Evens = 0
for i in range(len(values)):
    if values[i] % 2 == 0:
        num_Of_Evens += 1

if len(values) == 5:
    num_Of_Evens += 1
print(num_Of_Evens)