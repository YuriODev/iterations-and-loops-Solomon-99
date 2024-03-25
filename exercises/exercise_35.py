def print_odd_numbers(n):
    start = 10**(n-1)
    end = 10**n - 1

    if start % 2 == 0:
        start += 1

    for num in range(end, start - 1, -2):
        print(num, end=" ")

digits = int(input())
print_odd_numbers(digits)
