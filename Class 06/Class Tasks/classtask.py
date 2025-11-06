# # Temperature Task

# curr_temp = int(input("Enter the current temperature : "))
# if curr_temp < 0 :
#     print("Freezing")
# elif curr_temp <= 15 :
#     print("Cold")
# elif curr_temp <= 30 :
#     print("Warm")
# else : print("Hot")

# # Even, Odd or Zero
# num = int(input("Enter a number : "))
# if num == 0 :
#     print("Zero")
# elif num % 2 == 0 :
#     print("Even")
# else : print("Odd")

# # Grade calculator

# perc = int(input("Enter your percentage : "))

# if perc >= 90 :
#     print("A Grade")
# elif perc >= 80 :
#     print("B Grade")
# elif perc >= 70 :
#     print("C Grade")
# elif perc >= 60 :
#     print("D Grade")
# else : print("Fail")

# # Leap Year Check

# year = int(input("Enter year : "))

# if year % 4 == 0 :
#     print("It is a leap year")
# elif year % 400 == 0 :
#     print("It is a leap year")
# else : print("It is not a leap year")

# # Simple Login System

# username = input("Enter your username : ")
# password = input("Enter your password : ")

# def_username = "Azaan"
# def_password = "1234"

# if username == def_username :
#     if password == def_password :
#         print("Login Successful")
#     else : print("Incorrect password")
# else : print("Access Denied")

# # Number comparision

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))

# if num1 > num2 and num1 > num3:
#     print("Number 1 is the Largest Number")
#     if num2 > num3:
#         print("Number 3 is the smallest")
#     else : print("Number 2 is the smallest")
# elif num2 > num1 and num2 > num3:
#     print("Number 2 is the Largest Number")
#     if num1 > num3:
#         print("Number 3 is the smallest")
#     else: print("Number 1 is the smallest")
# elif num3 > num1 and num3 > num2:
#     print("Number 3 is the Largest Number")
#     if num1 > num2:
#         print("Number 2 is the smallest")
#     else: print("Number 1 is the smallest")

# # Traffic Light Simulator

# color = input("Enter a color (Red, Yellow or Green) : ")

# if color.lower() == "red" :
#     print("Stop")
# elif color.lower() == "yellow" :
#     print("Ready to go")
# elif color.lower() == "green" :
#     print("Go")
# else : print("Only red yellow and green colors are acceptable")