# Bianca Pallaro
# Monday, October 26, 2020
# "Homework 1"


year_birth = input("What year were you born?")
year_birth = int(year_birth)

#Ask the user the year they were born. 
# Convert it to an integer. 
# If they write a smaller year than 2020 (which should be the correct response), subtract it by 2020 to found out their age.
# Else, just ask him again and expect him to give you the right response.
if year_birth < 2020:
    print(f'You are {2020 - year_birth}')
else:
    year_birth = input("What year were you born?")
    year_birth = int(year_birth)
    print(f'You are {2020 - year_birth}')

#The heart beats about 100,000 times in one day and about 35 million times in a year 
#So we will need to do the age times 35 million
age = 2020 - year_birth
print(f'Your heart has beaten {age*35000000}')

#A blue whale's heart beats 4204800 times in a year

print(f'A blue whales heart has beaten {age*4204800} times during your lifetime')

#A rabbit's heart beats between 140 and 180 per minute. If we multiply 160 times the amount of minutes in a year (525600), that is 84096000.

rabbit = age*84096000
if rabbit > 1000000:
    print(f'A rabitts heart has beaten {round(rabbit/1000000)} million times during your lifetime')

#It takes 225 Earth days for Venus to go all the way around the sun

venus= (age*365)/225
print(f'You are {round(venus)} in Venus Years')

#A year on Neptune lasts as long as about 165 years here on Earth

neptune = age/165 
print(f'You are {round(neptune, 2)} in Neptune Years')

#If your are the same page, print "You are the same age as me".
#Else if your younger, print "You are older"
#Else print "You are younger"

if age == 26:
    print("You are the same age as me!")
elif age < 26:
    print(f'You are {26-age} younger than me!')
else:
    print(f'You are {age-26} older than me')

#If they were born in an even or odd year. If x % 2 == 0 it's an even number
if year_birth % 2 == 0:
    print("You were born in an even year")
else:
    print("You were born in an odd year")

#How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)

if year_birth > 1960 and year_birth < 1963:
    print("There has been 5 democratic president")
elif year_birth > 1963 and year_birth < 1977:
    print("There has been 4 democratic presidents")
elif year_birth > 1977 and year_birth < 1993:
    print("There has been 3 democratic presidents")
elif year_birth > 1993 and year_birth < 2009:
    print("There has been 2 democratic presidents")
elif year_birth > 2009 and year_birth < 2016:
    print("There has been 1 democratic presidents")
else:
    print("No democratic presidents")

#Presidents between terms

if year_birth > 1960 and year_birth < 1963:
    print("Kennedy")
elif year_birth > 1963 and year_birth < 1969:
    print("Johnson")
elif year_birth > 1969 and year_birth < 1974:
    print("Nixon")
elif year_birth > 1974 and year_birth < 1977:
    print("Ford")
elif year_birth > 1977 and year_birth < 1981:
    print("Carter")
elif year_birth > 1981 and year_birth < 1989:
    print("Reagen")
elif year_birth > 1989 and year_birth < 1993:
    print("G.H.W.Bush")
elif year_birth > 1993 and year_birth < 2001:
    print("Clinton")
elif year_birth > 2001 and year_birth < 2009:
    print("G.W.Bush")
elif year_birth > 2009 and year_birth < 2017:
    print("Obama")
else:
    print("Trump")





























    
