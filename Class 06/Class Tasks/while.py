## Table Generator (Using while loop)

table = int(input("Enter table number: "))
i = 1

while i <= 10:
    print(f"{table} x {i} = {table * i}")
    i += 1

## Sum of Natural Numbers

n = int(input("Enter n: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)

## Count Digits in a Number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Total digits:", count)