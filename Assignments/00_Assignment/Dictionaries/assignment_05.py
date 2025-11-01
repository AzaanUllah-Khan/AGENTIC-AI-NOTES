# Task: Create a dictionary named students with nested dictionaries for each student's information, Loop through the students dictionary and print each student's name along with their grade.

students = {
    "Azaan" : {"age":16,"grade":"A+"},
    "Ahmed" : {"age":16,"grade":"A"},
    "Ibad" : {"age":14,"grade":"B"}
}

for i in students :
    print (i,students[i]["grade"])