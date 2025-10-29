name = "AzaanUllah Khan"
age = str(16) #It is casted as a string so even if it is 16 it will be considered as a string
print(type(age))
print("My name is",name,"and I am",age,"years old")


x,y,z = "Azaan","Ullah","Khan"
print(x) #Azaan
print(y) #Ullah
print(z) #Khan

x = y = z = "AzaanUllah Khan"
print(x) #AzaanUllah Khan
print(y) #AzaanUllah Khan
print(z) #AzaanUllah Khan


fruits = ["Banana","Apple","Cherry"]
print("Fruits:",fruits)

# Scope of variables

scope = "Global"
class function():
    scope = "Local"
    print(scope)
print(scope)

# List
Students = ["Azaan","Ali","Ahmed"]

#Tuple
Teachers = ("Rizwan","Shahmeer","Iqbal")

#Set
Visitor = {"Azaan","Ahmed","Ibad","Ahmed"}

#Dictionary
Attendance = {
    "name":"Azaan",
    "age" : 16,
    "skills" : ["HTML","CSS","JS"]
}
