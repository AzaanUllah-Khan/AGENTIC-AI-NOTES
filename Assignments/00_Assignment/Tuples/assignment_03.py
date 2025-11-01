# Task: Create a tuple of 10 numbers and print:

# The first 3 numbers
# The last 3 numbers
# The middle 4 numbers

numbers = (1,2,3,4,5,6,7,8,9,10)
first_3 = slice(0,3)
last_3 = slice(-3,None)
middle_4 = slice(3,7)

print(numbers)
print("First 03 numbers",numbers[first_3])
print("Last 03 numbers:",numbers[last_3])
print("Middle 04 numbers:",numbers[middle_4])