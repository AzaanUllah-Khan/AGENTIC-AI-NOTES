num1 = int(input("Enter First Number = "))
num2 = int(input("Enter Second Number = "))
num3 = int(input("Enter Third Number = "))

print("Sum", num1+num2)
print("Difference", num1-num2)
print("Product", num1*num2)
print("Division", num1/num2)
print("Square", num1**2)
print("Average", (num1+num2+num3)/3)

#------------------------
#Calculate simple interest

principal = int(input("Enter Principal = "))
rate = int(input("Enter rate = "))
time = int(input("Enter Time = "))

interest = (principal*rate*time)/100

print("Interest is", interest)

#-------------------------
#Calculate area

radius = int(input("Enter radius of the circle = "))
print("Area of circle is",(3.14)*(radius**2))

#-------------------------
#Swap variables

#Logic 1

swap1 = 50
swap2 = 100
diff = swap1-swap2
swap1 = (swap1+swap2)-swap1
swap2 = swap1+diff

print(swap1)
print(swap2)

#Logic 2

a = 10
b = 60

a = a+b #10+60 = 70
b = b-a #60-70 = -10
a = b+a #-10+70 = 60
b = -b #-(-10) = 10

print(a,b)

#Logic 3

x = 10
y = 20

x,y = y,x

print(x,y)