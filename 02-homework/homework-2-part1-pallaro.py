# Bianca Pallaro
# Thursday, October 29, 2020
# Homework 2, Part 1

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22,90,0,-10,3,22,48]
# Display the number of elements in the list.
print(len(numbers))
#Display the 4th element of this list.
print(numbers[3])
#Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])
#Display the 2nd-largest value in the list.
sort_numbers = sorted(numbers)
print(sort_numbers[-2])
#Display the last element of the original unsorted list
print(numbers[-1])
#Display the sum of all of the numbers divided by two.
print(sum(numbers)/2)
#Print whether the median or the mean of the numbers is higher
mid= round(len(sort_numbers) / 2)
median= (sort_numbers[mid])
amount= len(numbers) 
total = sum(numbers)
mean = round(total/amount)

if median > mean:
    print("Median:", median, "is higher than the mean:", mean)
else: 
    print("Mean:", mean, "is higher than the median:", median)


# Define a dictionary called movie that works with the following code.

movie = {'title': 'Lion King','year': '1994','director': 'Roger Allers' }
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#On the lines after that, add keys to the movie dictionary for budget and revenue 
# (you'll use code like movie['budget'] = 1000), 
# and print out the difference between the two.

movie['budget'] = 45000000
movie['revenue'] = 766000000
difference = (movie['revenue'] - movie['budget'])
print(difference)

#3) If the movie cost more to make than it made in theaters, print 
# "That was a bad investment". If the film's revenue was more than five times 
# the amount it cost to make, print "That was a great investment." 
# Otherwise print "That was an okay investment."

if movie['budget'] > movie['revenue']:
    print('That was a bad investment')
elif movie['revenue'] > (movie['budget']*5):
    print('That was a great investement')
else:
    print('That was an okay investment')

#4) Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, 
# Queens has 2.3m and Staten Island has 470,000. (
# Tip: keeping it all in either millions or thousands is a good idea)

nyc = {
    'Manhattan': 1600000,
    'Brooklyn': 2600000,
    'Bronx': 1400000,
    'Queens': 2300000,
    'Staten Island' : 470000
}
# 5) Display the population of Brooklyn.
print(nyc['Brooklyn'])
#6) Display the combined population of all five boroughs
pop_nyc = sum(nyc.values())
print(pop_nyc)
#7) Display what percent of NYC's population lives in Manhattan.
per_manhattan = round(((nyc['Manhattan'] / pop_nyc) * 100))
print(per_manhattan)


