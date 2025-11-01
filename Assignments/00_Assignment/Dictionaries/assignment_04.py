# Task: Create a dictionary of 3 products and their prices (e.g., {"apple": 1.5, "banana": 0.75, "orange": 1.2}). Ask the user which product's price they want to see and display it.

products = {
    "Apple" : 15,
    "Banana" : 10,
    "Mango": 35
}

name = input("Enter name of a fruit (Apple, banana, Mango) : ")
print(products[name])