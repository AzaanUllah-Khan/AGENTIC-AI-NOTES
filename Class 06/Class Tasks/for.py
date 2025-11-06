# # Class Example

# table = 2

# for i in range(1,11) :
#     print(f"{table} x {i} = {table*i}")


# # Sum of Natural Numbers

# n = int(input("Enter n : "))
# sum = 0

# for i in range(1,n+1) :
#     sum = sum+i

# print(sum)


# #Table Generator

# table = int(input("Enter number : "))

# for i in range(1,11) :
#     print(f"{table} x {i} = {table*i}")


# # Count vowels in a string

# str = input("Enter your name : ")
# vowels = 0

# for i in range(len(str)) :
#     if str[i].lower() == "a" or str[i].lower() == "e" or str[i].lower() == "i" or str[i].lower() == "o" or str[i].lower() == "u":
#         vowels += 1

# print("Your name has",vowels,"vowels")

# # Reserse the string

# str = "Azaan"
# newStr = ""

# for i in range(len(str),0,-1):
#     newStr += str[i-1]

# print(newStr)

# # Even numbers from the list

# list = [10,20,30,41,50]

# for i in range(0,len(list)) :
#     if list[i]%2 == 0:
#         print(list[i])