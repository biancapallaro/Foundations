# Bianca Pallaro
# Monday, November 2, 2020
# Homework 3, Part 2

# What is the URL to the documentation?
#https://www.weatherapi.com/docs/
# Make a request for the current weather where you are born, or somewhere you've lived.
import requests
url= "http://api.weatherapi.com/v1/current.json?key=2579d590d93542729e0192337200311&q=Buenos Aires"
response = requests.get(url, allow_redirects=True)
data = response.json()

print(data.keys())

# Print out the country this location is in.
print(data['location']['name'])

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
feels = data['current']['feelslike_c']
current = data['current']['temp_c']
print(f'It feels {round(feels - current)} degrees colder')

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
url2= "http://api.weatherapi.com/v1/current.json?key=2579d590d93542729e0192337200311&q=LHR"
response = requests.get(url2, allow_redirects=True)
data = response.json()
heathrow = data['current']['temp_c']
print(f'Current temperature at Heathrow is {round(heathrow)} degrees')

# What URL would I use to request a 3-day forecast at Heathrow?
url3 = "http://api.weatherapi.com/v1/forecast.json?key=2579d590d93542729e0192337200311&q=LHR&days=3"
response = requests.get(url3, allow_redirects=True)
data = response.json()

# Print the date of each of the 3 days you're getting a forecast for.
for three in data['forecast']['forecastday']:
    print(three['date'])

# Print the maximum temperature of each of the days.
date = data['forecast']['forecastday']
for three in date:
    print(three['day']['maxtemp_c'])
    
# Print the day with the highest maximum temperature.
highest_temp = 0 
highest_temp_date = ''
for day in date:
    if three['day']['maxtemp_c'] > highest_temp:
        highest_temp = three['day']['maxtemp_c']
        highest_temp_date = three['date']

print("The day with the highest max temperature", highest_temp, "is", highest_temp_date)


