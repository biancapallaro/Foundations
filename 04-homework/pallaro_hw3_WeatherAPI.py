#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[2]:


url= "http://api.weatherapi.com/v1/current.json?key=2579d590d93542729e0192337200311&q=Buenos Aires"
response = requests.get(url, allow_redirects=True)
data = response.json()


# In[5]:


(data.keys())


# In[6]:


data['location']['name']


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[10]:


data['current']['wind_mph']


# In[11]:


temperature = data['current']['temp_c']
feels = data['current']['feelslike_c']


# In[14]:


feels, temperature


# In[16]:


round(feels-temperature,1)


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[37]:


url1= "http://api.weatherapi.com/v1/astronomy.json?key=2579d590d93542729e0192337200311&q=Buenos Aires&dt=2020-11-12"
response = requests.get(url1, allow_redirects=True)
data = response.json()


# In[38]:


data.keys()


# In[39]:


data['astronomy']


# In[41]:


data['astronomy']['astro']['moon_illumination']


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[44]:


url2= "http://api.weatherapi.com/v1/forecast.json?key=2579d590d93542729e0192337200311&q=Buenos Aires&days=1"
response = requests.get(url2, allow_redirects=True)
data = response.json()


# In[54]:


forecast = data['forecast']['forecastday']
for forecas in forecast:
    max_temp = forecas['day']['maxtemp_c']
print(max_temp)


# In[55]:


forecast = data['forecast']['forecastday']
for forecas in forecast:
    min_temp = forecas['day']['mintemp_c']
print(min_temp)


# In[56]:


max_temp-min_temp


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# The name of the url variable. And rename the response. 

# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[72]:


url3 = "http://api.weatherapi.com/v1/forecast.json?key=2579d590d93542729e0192337200311&q=Buenos Aires&days=7"
response = requests.get(url3, allow_redirects=True)
data = response.json()


# In[73]:


forecast = data['forecast']['forecastday']


# In[74]:


for forecas in forecast:
    print(forecas['date'])
    print(forecas['day']['maxtemp_c'])
    if forecas['day']['maxtemp_c'] < 10:
        print('Cold')
    elif forecas['day']['maxtemp_c'] > 31:
        print('Hot')
    else:
        print('Warm')


# # 6) What will be the hottest day in the next week? What is the high temperature on that day?

# In[77]:


highest_temp = 0 
highest_temp_date = ''


# In[78]:


for forecas in forecast:
    if forecas['day']['maxtemp_c'] > highest_temp:
        highest_temp = forecas['day']['maxtemp_c']
        highest_temp_date = forecas['date']

print("The day with the highest max temperature", highest_temp, "is", highest_temp_date)


# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[80]:


url4 = "http://api.weatherapi.com/v1/forecast.json?key=2579d590d93542729e0192337200311&q=Miami&days=1"
response = requests.get(url4, allow_redirects=True)
data = response.json()


# In[84]:


forecast = data['forecast']['forecastday']
print(forecast)


# In[93]:


for forecas in forecast:
    hour = forecas['hour']
    for time in hour:
        times = time['time']
        temperature = time['temp_c']
        if time['cloud'] > 50:
            print(f"At {times} its going to be {temperature} degrees and cloudy")
        else:
            print(f"At {times} its going to be {temperature} degrees")
    


# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[99]:


counter = 0
for forecas in forecast:
    hour = forecas['hour']
    for time in hour:
        if time['temp_c'] > 30:
            counter = time['temp_c'] + 1
print(counter*100/24)


# I don't know farenheits, I just converted 85 to degrees. No temperature for those 24 hours is bigger that 30 degrees. 

# In[ ]:





# ## 9) What was the temperature in Central Park on Christmas Day, 2015? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*

# Free plan - Weather History (Last 7 days only)

# In[ ]:





# In[ ]:




