# Task: Store 4 movie names in a list. Print:

# The first two movies
# The last movie
# The total number of movies


movies = ["Stranger Things", "Five Feets Apart", "Midnight Sun", "If I Stay","Before I fall"]
print("First Two Movies",movies[slice(0,2)])
print("Last Two Movies",movies[slice(-2,None)])
print("Total Number of movies",len(movies))