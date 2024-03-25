num_Of_Days = int(input())
temperatures = []

for i in range(num_Of_Days):
    temp = int(input())
    temperatures.append(temp)

below_minus_15_degrees = "No"

for i in range(num_Of_Days):
    if temperatures[i] < -15:
        below_minus_15_degrees = "Yes"
        break

min = 0
for temp in temperatures:
    if temp < min:
        min = temp

print(f"{min}\n{below_minus_15_degrees}", end="")