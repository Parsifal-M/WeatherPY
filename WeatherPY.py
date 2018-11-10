#!/usr/bin/python3
# Prints the weather from the command line.
# From Automate the boring stuff.

import json
import requests

location = input("Enter the City: ")
countrycode = input("Enter country code: ")
# Getting the DATA
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s,%s&APPID=(KEY)' % (
    location, countrycode)
response = requests.get(url)
response.raise_for_status()

# Load JSON Data and make it readable.
weatherData = json.loads(response.text)

# Print weather.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]
      ['description'], '-' + '' + 'Wind: ', w[0]['wind']['speed'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]
      ['description'], '-' + '' + 'Wind: ', w[1]['wind']['speed'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]
      ['description'], '-' + '' + 'Wind: ', w[2]['wind']['speed'])
