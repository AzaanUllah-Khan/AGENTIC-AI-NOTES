# Task: Create two sets: A = {1, 2, 3, 4} B = {3, 4, 5, 6}

# Print their:

# Union (all unique elements from both sets)
# Intersection (elements common to both sets)
# Difference (elements in A but not in B)

A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}

Union = A.union(B) #1,2,3,4,5,6
Intersection = A.intersection(B) #3,4
Difference = A.difference(B) #1,2

print("Union :",Union)
print("Intersection :",Intersection)
print("Difference :",Difference)