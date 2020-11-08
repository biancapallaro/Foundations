# Bianca Pallaro
# Monday, November 2, 2020
# Homework 3, Part 1

#HI! :) I JUST WANT TO LET YOU KNOW THAT I COMMENTED EACH PART AS I WENT THROUGH THE EXCERCISES BECAUSE I DIDN'T KNOW HOW THE URLS WERE GOING TO WORK


# What is the URL to the documentation?
#https://pokeapi.co/docs/v2

# What pokemon has the ID of 55?
import requests
url= "https://pokeapi.co/api/v2/pokemon/55"
response = requests.get(url, allow_redirects=True)
data = response.json()
#print(data)
#print(data.keys())
print(data['name'])

# How tall is that pokemon?
print(data['height'])

# How many versions of Pokemon games have been released?
url= "https://pokeapi.co/api/v2/version/"
response = requests.get(url, allow_redirects=True)
data = response.json()
total = 0
for result in data['results']:
    total = total + 1
print("total versions", total)

# Print out the name of every electric-type pokemon.
url= "https://pokeapi.co/api/v2/type/electric/"
response = requests.get(url, allow_redirects=True)
data = response.json()
 #print(data.keys())
for poke in data['pokemon']:
    print(poke['pokemon']['name'])

# What are electric-type Pokemon called in the Korean version of the game?
url= "https://pokeapi.co/api/v2/type/electric/"
response = requests.get(url, allow_redirects=True)
data = response.json()
for poke in data['names']:
    lang = poke['language']
    if poke['language']['name'] == 'ko':
        print(poke['name'])


# Who has a higher speed stat, Eevee or Pikachu?
url= "https://pokeapi.co/api/v2/pokemon/eevee"
url2= "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url, allow_redirects=True)
eevee = response.json()
response = requests.get(url2, allow_redirects=True)
pikachu = response.json()

#print(data['stats'])
for stat in eevee['stats']:
    speed = stat['stat']
    if speed['name'] == 'speed':
        eevee_speed = (stat['base_stat'])

for stat in pikachu['stats']:
    speed = stat['stat']
    if speed['name'] == 'speed':
        pika_speed= stat['base_stat']

if pika_speed > eevee_speed:
    print("Pikachus speed", pika_speed, "is bigger than Evees", eevee_speed)
else:
    print("Eevees speed", eevee_speed, "is bigger than Pikachu", pika_speed)

