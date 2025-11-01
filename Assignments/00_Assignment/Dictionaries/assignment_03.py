# Task: Create a dictionary of 3 countries with their capitals (e.g., Pakistan: Islamabad, Turkey: Ankara, Japan: Tokyo). Loop through the dictionary and print each country and its capital in the format: Country → Capital.

countries = {
        "Australia":"Canberra",
        "Pakistan":"Islamabad",
        "Germany":"Berlin"
}

for i in countries :
    print(i,"→",countries[i])