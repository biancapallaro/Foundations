# Bianca Pallaro
# Thursday, October 29, 2020
# Homework 2, Part 2

#1) Make a list called "countries"
countries = ['United States','Argentina','Canada','Italy','Spain','France','Germany']

#2) Using a for loop, print each element of the list
for country in countries:
    print(country)

#3) Sort the list permanently.
countries.sort()
print(countries)

#4) Display the first element of the list.
print(countries [0])

#5) Display the second-to-last element of the list.
print(countries [5])

#6) Delete one of the countries from the list using its name.

countries.remove('Argentina')

print(countries)

# 7) Using a for loop, print each country's name in all caps.
for country in countries:
    upper = country.upper()
    print(upper)

#1) Make a dictionary called 'tree' 
tree = {
    'name': 'Glencoe Baobab',
    'species': 'Baobab',
    'age': 1835,
    'location_name': 'Hoedspruit, South Africa',
    'latitude': -24.373611,
    'longitude': 30.856667,
}
#2)Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(tree['name'], "is a", tree['age'], "year old tree that is in", tree['location_name'])

#3) The coordinates  

if 40.7128 < tree['latitude']:
    print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC")
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC")

#4) Ask the user how old they are. 
age = input("What is your age?")
age = int(age)

if age > tree['age']:
    print("You are",(age - tree['age']), "older than", tree['name'])
else:
    print(tree['name'], "was", (tree['age'] - age), "years old when you were born")

#1) Make a list of dictionaries of five places across the world 
# - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago.

places = [
    {'name': 'Moscow','latitude': 55.761590 ,'longitude': 37.609460 },
    {'name': 'Tehran','latitude': 35.668208,'longitude': 51.374414 },
    {'name': 'Falkland Islands','latitude': -51.796719,'longitude': -58.594932 },
    {'name': 'Seoul','latitude': 37.547895 ,'longitude': 126.941893  },
    {'name': 'Santiago','latitude': -33.445995 ,'longitude': -70.667057 },
]

#2) Loop through the list, printing each city's name and whether it is above 
#or below the equator (How do you know? Think hard about the latitude.). 
# When you get to the Falkland Islands, also display the message

for place in places:
    if place['latitude'] < 0:
        print(place['name'], "is below the equator")
        if place['name'] == 'Falkland Islands':
            print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    else:
        print(place['name'], "is above the equator")

#3) Loop through the list, printing whether each city is north of south of your 
# tree from the previous section.

for place in places:
    if place['latitude'] < tree['latitude']:
        print(place['name'], "is south of the tree:", tree['name'])
    else:
        print(place['name'], "is north of the tree:", tree['name'])



