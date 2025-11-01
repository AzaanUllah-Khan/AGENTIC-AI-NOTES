# Task: Make a list of 5 grocery items. Replace one item (e.g., change 'milk' to 'butter'). Print the updated list and the total number of items in the list.

shopping_list = ["Sugar","Salt","Milk", "Butter"]
shopping_list.insert(shopping_list.index("Milk"),"Yogurt")
shopping_list.remove("Milk")

print(shopping_list)